from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

from indexapp.models import UserModel
from .models import CitysModel
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


# 短信返回
def msg_code(request):
    phone = request.POST.get('phone')
    u_phone = UserModel.objects.filter(phone=phone)


    if u_phone:
        # 手机号保存在session
        request.session['phone'] = u_phone

        return JsonResponse({
            'code': 200,
            'msg': '短信验证码发送成功!'
        })
    else:
        return JsonResponse({
            'code': 303,
            'msg': '请输入正确的手机号码'
        })


# 检车手机号
def check_phone(request):
    phone = request.GET.get('phone')
    user = UserModel.objects.filter(phone=phone)
    if not user:
        return JsonResponse({
            'code': 200,
            'msg': '手机号不存在'
        })
    else:
        return JsonResponse({
            'code': 205,
            'msg': '手机号已存在'
        })


# 密码登录
def login_pwd(request):
    phone = request.POST.get('u_phone', None)
    pwd = request.POST.get('auth_string', None)

    phone = UserModel.objects.filter(phone=phone)

    if phone:
        phone = phone.first()
        if pwd != phone.pwd:
            return JsonResponse({
                "code": "303",
                "msg": "用户口令不正确"
            })
    else:
        return JsonResponse({
            'code': 304,
            'msg': '该手机尚未注册'
        })


# 验证码登录
def msg_login(request):
    phone = request.POST.get('u_phone', None)
    code = request.POST.get('msg_code', None)

    request.session['phone'] = phone
    request.session['code'] = code

    cache.set(phone, code)

    return JsonResponse({
        "code": 200,
        "token": "b8735a654d1442cf9025bf2b14e2a309",
        "user_data": {
            "balance": '',
            "gender": '',
            "id": 1,
            "idcard": '',
            "img": '',
            "is_active": 1,
            "is_delete": 0,
            "nickname": "YG18991708565",
            "u_auth_string": "123456",
            "u_level": '',
            "u_phone": "18991708565"
        }
    })


# 忘记密码
def forgot(request):
    return JsonResponse({
        "code": 200,
        "token": "8a72951e4cee4715a5667ead5566af57",
        "user_data": {
            "balance": '',
            "gender": '',
            "id": 1,
            "idcard": '',
            "img": '',
            "is_active": 1,
            "is_delete": 0,
            "nickname": "YG18991708565",
            "u_auth_string": "123456",
            "u_level": '',
            "u_phone": "18991708565"
        }
    })


def add_city(request):
    with open('city.json', 'r', encoding='utf-8') as f:
        city_dict = json.load(f)
        for i in city_dict['Data']['CityList']:
            for r in i['CityList']:
                CitysModel.objects.create(
                    name=r['AreaName'],
                    start_str=r['FirstLetter'],
                    is_popular=True
                )

    return HttpResponse('ok')
