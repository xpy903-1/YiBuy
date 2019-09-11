from django.db.models import Q
from django.http import JsonResponse

from .models import GoodsModel, SecClassify, FirstClassify


# Create your views here.



def query_goods_info(request, uid):
    goods = GoodsModel.objects.filter(uid=uid)
    if goods:
        good = goods.first()

        data = {
            "code": 200,
            "data_wheel": [
                {
                    "goods_id": good.uid,
                    "child_id":  good.cate_id.uid1,
                    "detail_name": good.detail,
                    "category_id": good.cate_id.uid2.uid,
                    "marketprice": good.market_price,
                    "name": good.name,
                    "price": good.goods_price,
                    "pro_addr": "原产地：{}".format(good.produce_place)
                }
            ],
            "msg": "ok"
        }
        return JsonResponse(data=data)

    else:
        data = {'code': 404, 'msg': 'not found'}

        return JsonResponse(data)




def query_goods_img(request, uid):
    # goods_id = request.GET.get('uid')
    goods = GoodsModel.objects.filter(uid=uid)

    if goods:
        good = goods.first()
        data = {
            "code":200,
            "data_wheel": [
                {
                    "detail_img_url": good.detail_img,
                    "cate_id": good.cate_id.uid1
                }
            ],
            "msg": "ok"
        }
        return JsonResponse(data=data)

    else:
        data = {'code': 404, 'msg': 'not found'}
        return JsonResponse(data=data)

def goodsclassfiy(request, fuid):
    fcms = FirstClassify.objects.filter(uid=fuid)
    if fcms:
        fcm = fcms.first().uid
        secs = SecClassify.objects.filter(uid2=fcm)
        if secs:
            secs = secs.all()
            data_list = []
            for sec in secs:
                data_dict = {
                    'child_id': sec.uid1.hex,
                    'child_name':sec.name
                }
                data_list.append(data_dict)

            data = {
                'code': 200,
                'msg': 'ok',
                'child_info': data_list
            }

            return JsonResponse(data=data)

    data = {'code': 404, 'msg': 'not found'}
    return JsonResponse(data=data)

def search(request):
    word = request.GET.get('word')
    infos = GoodsModel.objects.all().filter(Q(name__contains=word)|Q(description__contains=word))
    if infos:
        data_list = []
        for info in infos:
            data_dict = {
                "category_id": info.cate_id.uid2.uid,
                "category_name": info.cate_id.uid2.name,
                "child_id": info.cate_id.uid1,
                "child_name": info.cate_id.name
            }
            data_list.append(data_dict)

        data ={

                "code": 200,
                "data": {
                    "code": 200,
                    "datas": data_list,
                    "total": len(data_list)
                },
                "msg": "ok"
            }

        return JsonResponse(data=data)
    else:
        data = {'code': 404, 'msg': 'not found'}

        return JsonResponse(data=data)

