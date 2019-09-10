from django.http import JsonResponse,  response
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
    user_phone = request.POST.get('user_phone', None)
    user_pwd = request.POST.get('user_pwd', None)
    user_img1 = request.POST.get('user_img1', None)
    if not all((user_img1, user_phone, user_pwd),):
        pass


def loginout(request):
    token = request.COOKIES.get("token", None)
    if not token:
        return JsonResponse(
            ({
                'code': 304,
                'msg': '传入数据为空'
            })
        )
    else:
        response.delete_cookie('token')
        return JsonResponse(
            ({
                'code': 200,
                'msg': '退出成功！'
            })
        )

def upload_avator(request):
    pass
def img_url(request):
    pass
