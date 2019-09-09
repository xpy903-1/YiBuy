from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def detaios(request):
    token = request.COOKIES.get("token", None)
    user = request.POST.get("token", None)
    if not token:
        return JsonResponse({
            'code': 300,
            'msg': '用户未登录,请重新登陆'
        })
    else:
        return JsonResponse({
            'code': 200,
            'msg': '获取成功',
            'name': user.name,
            'gender': user.sex,
            'level': user.level,
        })


def change(request):
    user_name = request.POST.get('user_name', None)
def loginout( request):
    pass
def upload_avator(request):
    pass
def img_url(request):
    pass
