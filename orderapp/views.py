from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from goodsapp.models import SecClassify, FirstClassify


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

def order(request, addr_id, goods_id, goods_cnts):
    pass