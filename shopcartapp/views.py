import json

from django.contrib.auth.hashers import check_password
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .form import PictureForm
from goodsapp.models import GoodsModel
from indexapp.models import UserModel
from shopcartapp.models import ShopCarModel, PictureModel
from shopcartapp.shopcartapi import GoodsSerializer, ShopCartSerializer, PictureSerializer


class LoginView(View):
    # get 方式返回登录界面
    def get(self, request):
        return render(request, 'login.html')

    # post 验证用户密码是否正确
    def post(self, request):
        error_msg = '用户名输入错误'
        name = request.POST.get('name', None)
        pwd = request.POST.get('pwd', None)

        if not all((name, pwd)):
            error_msg = '用户名或密码不能为空'
        else:
            user_name = UserModel.objects.filter(name=name)
            # 判断用户名是否存在
            if user_name.exists():
                user = user_name.first()
                if check_password(pwd, user.pwd):
                    request.session['login_user'] = {
                        'id': user.id,
                        'name': user.name,
                        'phone': user.phone,
                    }
                    return redirect('/shopcart/hotgood')  # 重定向地址
                else:
                    error_msg = '密码错误，请重新输入'
            else:
                error_msg = '用户名不存在，请先注册'

        return render(request, 'login.html', locals())


@api_view(['GET', 'PUT', 'DELETE'])
class goods_api(View):
    def get(self, request):
        method = request.method
        is_selected = request.GET.get('is_selected', None)
        if method == 'GET':
            goods = GoodsModel.objects.filter(is_selected=is_selected).all()
            serializer = GoodsSerializer(goods, many=True)
            return Response(serializer.data)
        else:
            serializer = GoodsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.instance)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def shop_cart(request):
    login_user = request.session.get('login_user', None)
    if not login_user:
        return JsonResponse({
            'code': 100,
            'msg': '当前用户未登录'
        })
    dict = {}
    if not ShopCarModel.objects.exists():
        return JsonResponse({
            'code': 400,
            'msg': '购物车没有商品'
        })
    else:
        shopcar = ShopCarModel.objects.all().values()
        picture = PictureModel.objects.all().values()
        ser_shop = ShopCartSerializer(shopcar, many=True)
        ser_picture = PictureSerializer(picture, many=True)
        # shopcar = ShopCarModel.objects.values('id', 'good_id', 'user_id', 'count', 'is_selected')
        # picture = PictureModel.objects.values('picture_name', 'id', 'picture_path')
        # dict['cart_datas'] = list(shopcar)
        # dict['goods_detail'] = list(picture)

        return JsonResponse({
            'cart_datas': ser_shop.data,
            'ser_picture': ser_picture.data
        }, safe=False)


# 热门商品
def hot_goods(request):
    if not GoodsModel.objects.exists():
        return JsonResponse({
            'code': 400,
            'msg': '为找到热门商品'
        })
    else:
        sales_volume = GoodsModel.objects.filter(sales_volume__gte=20).values()  # 销量大于20
        ser = GoodsSerializer(sales_volume, many=True)
        return JsonResponse({
            'code': 200,
            'data': ser.data,
        })


# 精选商品
def is_goodsed(request):
    if not GoodsModel.objects.exists():
        return JsonResponse({
            'code': 400,
            'msg': '为找到精选商品'
        })
    else:
        is_selected = GoodsModel.objects.filter(is_selected=True).values()
        ser = GoodsSerializer(is_selected, many=True)
        return JsonResponse({
            'code': 200,
            'datas': ser.data,
            'msg': 'OK'
        })


@csrf_exempt
def goods_add(request):
    if request.method == 'POST':
        user_id = UserModel.objects.get(pk=request.POST.get('user_id', None))
        good_id = GoodsModel.objects.get(pk=request.POST.get('good_id', None))
        count = request.POST.get('count', None)
        if not all((user_id, good_id, count)):
            return JsonResponse({
                'code': 400,
                'msg': '请求的参数不完整'
            })
        # 添加 user_id, good_id
        add_data = ShopCarModel()
        add_data.user_id = user_id
        add_data.good_id = good_id
        add_data.count = count

        if ShopCarModel.objects.aggregate(cnt=Count('count')) > 1:
            add_data.count += count
        else:
            add_data.save()
        return JsonResponse({
            'code': 200,
            'msg': '添加成功',
            'data': {
                'user_id': add_data.user_id.name,
                'good_id': add_data.good_id.name,
                'count': add_data.count,
            }
        })

    else:
        return render(request, 'shopcart/goods_add.html')


@csrf_exempt
def goods_update(request):
    if request.method == 'POST':
        user_id = UserModel.objects.get(pk=request.POST.get('user_id', None))
        good_id = GoodsModel.objects.get(pk=request.POST.get('good_id', None))
        count = request.POST.get('count', None)
        if not all((user_id, good_id, count)):
            return JsonResponse({
                'code': 400,
                'msg': '参数不完整'
            })
        update_data = ShopCarModel.objects.get(pk=id)
        update_data.user_id = user_id
        update_data.good_id = good_id
        update_data.count = count
        update_data.save()
        return JsonResponse({
            'code': 200,
            'msg': 'ok',
            'data': {
                'user_id': update_data.user_id,
                'good_id': update_data.good_id,
                'count': update_data.count
            }
        })
    # return render(request, 'goods_add.html')


@csrf_exempt
def goods_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id', None)
        if id:
            d_good = ShopCarModel.objects.get(pk=id)
            d_good.delete()
            return JsonResponse({
                'code': 200,
                'msg': '商品删除成功'
            })
        else:
            return JsonResponse({
                'code': 400,
                'msg': '请求的商品ID不存在'
            })
    # else:
    #     return render(request, 'adsdelete.html')

# def add_shopcart(request, id):
# login_user = request.session.get('login_user', None)
#     # if not login_user:
#     #     return JsonResponse({
#     #         'code': 100,
#     #         'msg': '当前用户未登录'
#     #     })

# try:
#     now_goods = GoodsModel.objects.get(id=id)
# except:
#     now_goods = None
# dict = {}
# dict['now_goods'] = now_goods
# if not now_goods:
#     return render(request, 'login.html', locals())
# # 获取 cookie 中的购物车 id
# good_id = request.COOKIES.get('good_id')
# try:
#     car_goods = ShopCarModel.objects.get(good_id=good_id)
#     car_goods.add_quantity()
# except:
#
# if request.method == 'POST':
#     # 新建商品
#     if 'Creat' in request.POST:
#         if PictureModel.objects.filter(id=request.POST['id']):
#             return HttpResponseRedirect('/shopcart/%s/' % str(request.POST['id'] + 'C'))
#         else:
#             new_car = PictureForm(request.POST)
#             if new_car.is_valid():
#                 save_new = new_car.save(commit=False)
#                 save_new.id = request.POST['id']
#                 save_new.save()
#                 return HttpResponseRedirect('/shopcart/%s/' % str(request.POST['id'] + 'E'))
#
#     # 修改商品
#     elif 'Update' in request.POST:
#         PictureModel.objects.filter(id=request.POST['id']) \
#             .update(picture_name=request.POST['picture_name'],
#                     picture_path=request.POST['picture_path'],
#                     picture_width=request.POST['picture_width'],
#                     picture_height=request.POST['picture_height'])
#         return HttpResponseRedirect('/shop_cart/%s/' % str(request.POST['id'] + 'U'))
#
#     # 添加到购物车
#     elif 'AddCar' in request.POST:
#         InputCar = ShopCarModel.objects.filter(id=request.POST['id'],
#                                                good_id=request.POST['good_id'],
#                                                user_id=request.POST['user_id'],
#                                                count=request.POST['count'],
#                                                is_selected=request.POST['is_selected'])
#         InputCar.save()
#         return HttpResponseRedirect('/shop_cart/%s/' % str(request.POST['id'] + 'A'))
#
#     # 购买
#     elif 'BuyGood' in request.POST:
#         request.session['id'] = request.POST['id']
#         request.session['good_id'] = request.POST['good_id']
#         request.session['user_id'] = request.POST['user_id']
#         request.session['count'] = request.POST['count']
#         request.session['is_selected'] = request.POST['is_selected']
#         return HttpResponseRedirect('/shop_cart/buygood/')
#     else:
#         return HttpResponseRedirect('/buygood')
#
# else:
#     if id[-1] == 'C':
#         types = '已存在'
#     elif id[-1] == 'E':
#         types = '已新增'
#     elif id[-1] == 'U':
#         types = '已加入购物车'
#     elif id[-1] == 'A':
#         types = '已修改购物车'
#     else:
#         types = ''
#     FormValue = PictureModel.objects.filter(id=id[0:4])[0]
#     FormValue = PictureForm({'id':id, 'picture_name': FormValue.picture_name,
#                              'picture_path': FormValue.picture_path,
#                              'picture_width': FormValue.picture_width,
#                              'picture_height':FormValue.picture_height})
#     return render(request, 'shop_cart.html', {'form': FormValue, 'types':types})
