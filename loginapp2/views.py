from django.http import JsonResponse,  response
from django.shortcuts import render

# Create your views here.
from indexapp.models import UserModel


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
    user_name = request.POST.get('user_name',None)
    user_phone = request.POST.get('user_phone', None)
    user_pwd = request.POST.get('user_pwd', None)
    user_img1 = request.FILES.get('user_img1', None)
    if user_img1:
        if all((user_img1.content_type.startswith('image/'),
                user_img1.size < 50 * 1024)):
            return
    user = UserModel.objects.get(user_name == 'name')
    if user:
        user = user.fist()
        if not all((user_img1, user_phone, user_pwd)):
            user.phone = user_phone
            user.pwd = user_pwd
            user.img1 = user_img1

            user.save()


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
        request.session.clear()
        resp = JsonResponse(
            ({
                'code': 200,
                'msg': '退出成功！'
            })
        )
        resp.delete_cookie('token')
        return resp

def upload_avator(request):
    pass
def img_url(request):
    pass
