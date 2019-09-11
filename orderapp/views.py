import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from addressapp.models import AddressModel
from goodsapp.models import SecClassify, FirstClassify, GoodsModel
from indexapp.models import UserModel
from orderapp.models import OrderModel
from signal import login_yz


def daohang(request, child_id, id):
    data = []
    list1 = SecClassify.objects.get(pk=child_id).goods.all()
    if id == '0':
        list1 = list1.order_by('sales_volume')
    elif id == '1':
        list1 = list1.order_by('storage')
    elif id == '2':
        list1 = list1.order_by('goods_price')
    for i in list1:
        d = {
            'detail_name': i.detail,
            'goods_img': i.goods_img,
            'id': i.id,
            'marketprice': i.market_price,
            'name': i.name,
            'price': i.goods_price,
            'pro_addr': i.produce_place
        }
        data.append(d)
    return JsonResponse({
        'code': 200,
        'datas': data,
        'msg': 'ok'
    })

def feilei(request, category_id):
    list1 = FirstClassify.objects.get(pk=category_id).secclass.all()
    b = []
    for i in list1:
        d = {
            'detail_img_url': i,
            'id':i.id,
            'name': i.name
        }
        b.append(d)
    return JsonResponse({
        'code': 8000,
        'data_wheel': b,
        'msg': 'ok'
    })

def order(request):
    uid = login_yz.send(sender='seven', request=request)[0][1]
    if not uid:
        return JsonResponse({
            'code':300,
            'msg':'请先登录'
        })
    uid = UserModel.objects.get(pk=uid)
    addr_id = AddressModel.objects.get(pk=request.POST.get('addr_id'))
    goods_id = GoodsModel.objects.get(pk=request.POST.get('goods_id'))
    goods_cnts = int(request.POST.get('goods_cents'))
    new_order = OrderModel.objects.create(
        count=goods_cnts,
        address_id=addr_id,
        goods_id=goods_id,
        user_id=uid,
        order_status=1
    )
    return JsonResponse({
        'code':200,
        'order_id':new_order.id,
        'total_price':new_order.total,

    })
    
def order_test(request):
    #实验用！
    if not login_yz.send(sender='seven', request=request)[0][1]:
        return HttpResponse('请先登录')
    a = AddressModel.objects.get(pk='5f630ecc-ef56-4066-90e3-eed3b01150fe')
    g = GoodsModel.objects.get(pk='ffcc0908-cb01-4311-bfaa-651bff372982')
    u = UserModel.objects.get(pk='8370030c-a3ef-4ff3-8c8b-7005e680120a')
    # print(a, '*'*100)
    # print(g, '*'*100)
    # print(u, '*'*100)
    OrderModel.objects.create(
        count=10,
        address_id=a,
        goods_id=g,
        user_id=u,
        order_status=1
    )
    return HttpResponse('ok')