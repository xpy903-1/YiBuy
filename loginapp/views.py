from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def msg_code(request):
    u_phone = request.POST.get('u_phone')


def check_phone(request):
    phone = request.POST.get('phone')
    if phone in cache:
        return JsonResponse({
            'code': 205,
            'msg': '手机号已存在'
        })
    else:
        return JsonResponse({
            'code': 200,
            'msg': '手机号不存在'
        })


def login_pwd(request):
    u_phone = request.POST.get('u_phone')
    auth_string = request.POST.get('auth_string')

    if any((cache.has_key(u_phone),
            cache.get(u_phone) == auth_string)):
        return JsonResponse({
            "code": "303",
            "msg": "用户口令不正确"
        })
    else:
        return JsonResponse({
            'code': 304,
            'msg': '该手机尚未注册'
        })


def msg_login(request):
    pass


def forgot(request):
    return render(request, '', locals())


