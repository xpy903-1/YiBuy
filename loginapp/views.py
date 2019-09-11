import uuid

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
    user = UserModel.objects.filter(phone=phone)

    if user:
        # 手机号保存在session
        request.session['phone'] = user

        return JsonResponse({
            'code': 200,
            'msg': '短信验证码发送成功!'
        })
    else:
        return JsonResponse({
            'code': 303,
            'msg': '请输入正确的手机号码'
        })


# 检查手机号
def check_phone(request):
    phone = request.GET.get('phone')
    u_phone = UserModel.objects.filter(phone=phone)

    if not u_phone:
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
        return render(request, 'login1.html')
    phone = request.POST.get('u_phone', None)
    pwd = request.POST.get('auth_string', None)

    phone = UserModel.objects.filter(phone=phone)

    if phone:
        phone = phone.first()
        if pwd != phone.pwd:
            return JsonResponse({
                "code": 303,
                "msg": "用户口令不正确"
            })
        else:
            token = uuid.uuid4().hex
            response = JsonResponse({
                'code':200,
                'msg':'成功'
            })
            response.set_cookie('token', token, expires=60*10)
            request.session['token'] = phone.id
            return response
    else:
        return JsonResponse({
            'code': 304,
            'msg': '该手机尚未注册'
        })


# 验证码登录
def msg_login(request):
    phone = request.POST.get('u_phone', None)
    code = request.POST.get('msg_code', None)
    # 生成token
    token = uuid.uuid4().hex
    # 保存在session
    request.session['phone'] = phone
    request.session['code'] = code

    user_data = UserModel.objects.all()

    data = {
        "balance": '',
        "gender": '',
        "id": 1,
        "idcard": '',
        "img": user_data.img1,
        "is_active": user_data.is_life,
        "is_delete": 0,
        "nickname": "YG18991708565",
        "u_auth_string": "123456",
        "u_level": '',
        "u_phone": "18991708565"
    }


# 忘记密码
def forgot(request):
    return render(request, '', locals())



