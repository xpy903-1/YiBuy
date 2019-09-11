from django.http import JsonResponse

from goodsapp.models import GoodsModel, FirstClassify
from loginapp.models import EntertainmentModel
from loginapp2.models import NavigationDetaiModel, CarsouseiMapModel
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
            if j < 2:
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
            "name": lei.name,
            "listimg": list
        }
        list1.append(data)
    wheel_pics = CarsouseiMapModel.objects.all()
    wheel_pic_list = []
    for wheel_pic in wheel_pics:
        pic = {
            "id": wheel_pic.id,
            "img": str(wheel_pic.img1),
            "name": wheel_pic.img_name,
        }
        wheel_pic_list.append(pic)
    nav_pics = NavigationDetaiModel.objects.all()
    nav_pic_list = []
    nav_good_list = []
    for nav_pic in nav_pics:
        nav_good = nav_pic.goods_id
        goods = {
            "detail_name": nav_good.detail,
            "goods_img": str(nav_good.goods_img),
            "id": nav_good.uid,
            "marketprice": nav_good.goods_price,
            "name": nav_good.name,
            "price": nav_good.market_price
        }
        nav_good_list.append(goods)
        data = {
            "nav_name": nav_pic.img_name,
            "nav_img": str(nav_pic.img1),
            "goods_img": nav_good_list
        }
        nav_pic_list.append(data)
    return JsonResponse({
        "code": 8000,
        "data_wheel": wheel_pic_list,
        "data_nav": nav_pic_list,
        "img_chosen_otherdata": list1,
        "msg": "ok"
    })


def navigation(request):
    nav_pics = NavigationDetaiModel.objects.all()
    nav_pic_list = []
    nav_good_list = []
    for nav_pic in nav_pics:
        nav_good = nav_pic.goods_id
        goods = {
            "detail_name": nav_good.detail,
            "goods_img": str(nav_good.goods_img),
             "id": nav_good.uid,
            "marketprice": nav_good.goods_price,
            "name": nav_good.name,
            "price": nav_good.market_price
        }
        nav_good_list.append(goods)
        data = {
            "nav_name": nav_pic.img_name,
            "nav_img": str(nav_pic.img1),
            "goods_img": nav_good_list
        }
        nav_pic_list.append(data)
    return JsonResponse({
        "code": 8000,
        "data_nav": nav_pic_list,
        "msg": "ok"
    })


def eats(request):
    wheel_pics = CarsouseiMapModel.objects.all()
    wheel_pic_list = []
    wheel_good_list = []
    for wheel_pic in wheel_pics:
        pic = {
            "eat_content": wheel_pic.img_name,
            "eat_img": str(wheel_pic.img1),
        }
        wheel_pic_list.append(pic)
        wheel_good = wheel_pic.goods_id
        goods = {
            "eat_content": wheel_good.description,
            "eat_img": str(wheel_good.goods_img),
            "eat_time": wheel_good.register_time
        }
        wheel_good_list.append(goods)

    return JsonResponse({
        "code": 8000,
        "data_wheel": wheel_pic_list,
        "img_eat_datas": wheel_good_list,
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
        if i.is_selected:
            data = {
                "detail_name": i.detail,
                "goods_img": i.goods_img,
                "id": i.uid,
                "name": i.name,
                "price": i.goods_price
            }
            list.append(data)
    return JsonResponse({
        "code": 200,
        "datas1": list,
        "msg": "ok"
    })
