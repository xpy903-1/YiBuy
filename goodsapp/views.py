from django.http import JsonResponse, HttpResponse

from .models import GoodsModel

import json
from goodsapp.models import SecClassify
# Create your views here.



def query_goods_info(request):
    goods_id = request.GET.get('uid')
    goods = GoodsModel.objects.filter(uid=goods_id)
    if goods:
        good = goods.first()
        data = {
            "code": 8000,
            "data_wheel": [
                {
                    "child_id": good.uid,
                    "detail_name": good.detail,
                    "cate_id": good.cate_id,
                    "marketprice": good.market_price,
                    "name": good.name,
                    "price": good.goods_price,
                    "pro_addr": "原产地：{}".format(good.produce_place)
                }
            ],
            "msg": "ok"
        }
        return JsonResponse(data=data)
        # return render(request, 'y.html', locals())
    else:
        data = {'code': 404, 'msg': 'not found'}
        return JsonResponse(data=data)

def query_goods_img(request):
    goods_id = request.GET.get('uid')
    goods = GoodsModel.objects.filter(uid=goods_id)
    if goods:
        good = goods.first()
        data = {
            "code": 8000,
            "data_wheel": [
                {
                    "detail_img_url": good.detail_img,
                    "cate_id": good.cate_id
                }
            ],
            "msg": "ok"
        }
        return JsonResponse(data=data)
        # return render(request, 'y.html', locals())
    else:
        data = {'code': 404, 'msg': 'not found'}
        return JsonResponse(data=data)

def goodsclassfiy(request):
    # goods_id = request.GET.get('uid')
    goods = GoodsModel.objects.filter(uid='ba2d93f5-3b25-4457-85ca-b933ad26d528')
    if goods:
        good = goods.first()
        data = {

                "child_type_datas": [
                    {
                        "child_id": good.uid,
                        "child_img": good.goods_img,
                        "child_name": good.cate_id.name
                    },

                ],
                "code": 8000,
                "msg": "ok",
                "type_detail_datas": [
                    {
                        "category_id": good.cate_id.uid2.uid,
                        "category_name": good.cate_id.uid2.name,
                        "id": 1
    },
            ],
            "msg": "ok"
        }
        return JsonResponse(data=data)

        # return render(request, 'y.html', locals())
    else:
        data = {'code': 404, 'msg': 'not found'}
        return JsonResponse(data=data)

def adddata(request):


    with open('data.json', 'r', encoding='utf-8') as f:
        r = json.load(f)
        for f in r:
            for i in f['Data']['CommodityList']:
                SecClassify.objects.get(pk='1eac57c4-59b4-4269-b018-6d2748f2e70a').goods.create(
                    goods_img=i['SmallPic'],
                    name=i['CommodityName'],
                    goods_price=i['OriginalPrice'],
                    sales_volume=i['MaxLimitCount'],
                    storage=100,
                    market_price=i['SellPrice'],
                    produce_place='西安',
                    detail_img=i['SmallPic'],
                    description=i['SubTitle'],
                    detail=i['SubTitle'],
                    is_selected=i['CanAddToCart']
                )

    return HttpResponse('ok')