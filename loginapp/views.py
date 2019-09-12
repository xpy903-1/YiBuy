import uuid

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

from indexapp.models import UserModel
from .models import CitysModel
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


# 检查手机号
def check_phone(request):

    data = request.body
    phone = data.get('phone')
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
@csrf_exempt
def login_pwd(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    data = json.loads(request.body.decode())
    phone = data.get('u_phone', None)
    pwd = data.get('auth_string', None)
    phone = UserModel.objects.filter(phone=phone).first()
    if phone:
        if pwd != phone.pwd:
            return JsonResponse({
                "code": 303,
                "msg": "用户口令不正确"
            })
        else:
            token = uuid.uuid4().hex
            response = JsonResponse({
                'code': 200,
                'msg': '登录成功'
            })
            response.set_cookie('token', token, expires=60 * 10)
            request.session[token] = phone.id
            return response
    else:
        return JsonResponse({
            'code': 304,
            'msg': '该手机尚未注册'
        })

