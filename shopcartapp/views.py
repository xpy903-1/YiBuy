from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response

from goodsapp.models import GoodsModel
from indexapp.models import UserModel
from shopcartapp.models import ShopCarModel, PictureModel


class LoginView(View):
    # get 方式返回登录界面
    def get(self, request):
        return render(request, 'login.html')

    # post 验证用户密码是否正确
    def post(self, request):
        error_msg = '用户名输入错误'
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)

        if not all((name, password)):
            error_msg = '用户名或密码不能为空'
        else:
            user_name = UserModel.objects.filter(name=name)
            # 判断用户名是否存在
            if user_name.exists():
                user = user_name.first()
                if check_password(password, user.pwd):
                    request.session['login_user'] = {
                        'id': user.id,
                        'name': user.name,
                        'phone': user.phone,
                    }
                    return redirect('/shopcart/newgoods')  # 重定向地址
                else:
                    error_msg = '密码错误，请重新输入'
            else:
                error_msg = '用户名不存在，请先注册'

        return render(request, 'login.html', locals())


def new_goods(request):
    goods = GoodsModel.objects.filter(is_goodsed=True).values()
    print([name for name in goods])
    return JsonResponse({
        "code": 200,
        "datas": {
            "detail_name": [description for description in goods],
            "goods_img": [goods_img for goods_img in goods],
            "id": [uid for uid in goods],
            "name": [name for name in goods],
            "price": [goods_price for goods_price in goods],
        }
    })


def car_goods(request):
    shopcar = ShopCarModel.objects.values()
    picture = PictureModel.objects.values()
    goods = GoodsModel.objects.values()
    return JsonResponse({
        "cart_datas": [{
            "c_goods_id": [id for id in shopcar],
            "c_goods_num": [good_id for good_id in shopcar],
            "c_user_id": [user_id for user_id in shopcar],
            "goods_detail": {
                "goods_img": [picture_path for picture_path in picture],
                "id": [id for id in picture],
                "name": [picture_name for picture_name in picture],
                "price": [goods_price for goods_price in goods]
            },
            "id": [id for id in shopcar]
        }]
    })

# def car_goods(request):
#     # 返回所有的购物车的 json 数据
#     result = {}
#     if ShopCarModel.objects.exists() and PictureModel.objects.values.exists():
#         datas = ShopCarModel.objects.values()
#         pictures = PictureModel.objects.values()
#         car_list = []
#         picture_list = []
#         for store in datas:
#             car_list.append(store)
#             for picture in pictures:
#                 picture_list.append(picture)
#                 result['goods_detail'] = picture_list
#         result['cart_datas'] = car_list
#
#     else:
#         result['msg'] = '没有数据!!!'
#
#     return JsonResponse(result)
