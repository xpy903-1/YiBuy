from django.http import JsonResponse

from goodsapp.models import GoodsModel, FirstClassify
from loginapp.models import EntertainmentModel
from loginapp2.models import NavigationDetaiModel
from addressapp.models import DiscountModel
from goodsapp.models import SecClassify


def home_page(request):
    leis = SecClassify.objects.all()
    list1 = []
    for lei in leis:
        goods1 = lei.goods.all()
        list = []
        j = 0
        for i in goods1:
            if j < 5:
                data = {
                    "detail_name": i.description,
                    "goods_img": i.goods_img,
                    "id": i.uid,
                    "marketprice": i.market_price,
                    "name": i.name,
                    "price": i.goods_price,
                }
                list.append(data)
                j += 1
            else:
                break
        data = {
            "id": lei.uid1,
            "img": lei.img,
            "listimg": list
        }
        list1.append(data)

    return JsonResponse({
        "code": 8000,
        "data_chosen": list1
    })


def index(request, category_id):
    goods_list = GoodsModel.objects.all()
    list11 = []
    for i in goods_list:
        goods = {
            "detail_name": i.detail,
            "goods_img": str(i.goods_img),
            "id": i.uid,
            "marketprice": i.goods_price,
            "name": i.name,
            "price": i.market_price
        }
        list11.append(goods)
    return JsonResponse({
        "code": 8000,
        "data_nav": list11,
        "msg": "ok"
    })


def eats(request):
    login_list = EntertainmentModel.objects.all()
    login2_list = NavigationDetaiModel.objects.all()
    list1 = []
    list2 = []
    for i in login2_list:
        data2 = {
            "eat_content": i.img_name,
            "eat_img": str(i.img1)
        }
        list2.append(data2)
    for i in login_list:
        data1 = {
            "eat_content": i.description,
            "eat_img": str(i.picture),
            "eat_time": i.time
        }
        list1.append(data1)
    return JsonResponse({
        "code": 8000,
        "data_wheel": list2,
        "img_eat_datas": list1,
        "msg": "ok"
    })


def member_show(request):
    disct = DiscountModel.objects.all()
    goods = GoodsModel.objects.all()
    list = []
    for i in disct:
        data = {
            "child_name": i.discount_amout,
            "detail_name": i.threshold,
            "id": i.id,
        }
        list.append(data)
    for i in goods:
        data = {
            "goods_img": i.goods_img,
            "name": i.name,
            "price": i.goods_price
        }
        list.append(data)
    return JsonResponse({
        "code": 200,
        "img_datas": list,
        "msg": "ok"
    })


def page_welfare(request):
    goods_list = GoodsModel.objects.all()
    list = []
    for i in goods_list:
        data = {
            "detail_name": i.detail,
            "goods_img": i.goods_img,
            "id": i.uid,
            "name": i.name,
            "price": i.goods_price
        }
        list.append(data)
    # first_class = FirstClassify.objects.all()
    # datas1 = first_class.name
    return JsonResponse({
        "code": 200,
        "datas1": list,
        "msg": "ok"
    })
