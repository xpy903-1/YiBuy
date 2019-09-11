import os
import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from indexapp.models import UserModel
from django.core.cache import cache


def detaios(request):
    if request.method == "POST":
        token = request.COOKIES.get("token", None)
        user = cache.get(token)
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
    user_phone = request.POST.get('user_phone', None)
    user_pwd = request.POST.get('user_pwd', None)
    if not all((user_name, user_pwd, user_phone)):
        return JsonResponse({
            'code': 300,
            'msg': '数据不能为空'
        })
    user = UserModel.objects.filter(name=user_name)
    if user:
        user = user.first()
        if not all((user_phone, user_pwd)):
            user.phone = user_phone
            user.pwd = user_pwd
            user.save()
            return JsonResponse({
                'code': 200,
                'msg': '修改信息成功'
            })
    return JsonResponse({
        'code': 300,
        'msg': '没有找到用户'
    })


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


@csrf_exempt
def upload_avator(request):
    token = request.COOKIES.get('token')
    if request.method == "Post":
        user_id = cache.get(token)
        user = UserModel.objects.filter(id=user_id).first()
        key = user.name
        upload_file: InMemoryUploadedFile = request.FILES.get('img1')
        if upload_file:
            if all((
                    upload_file.content_type.startswith('image/'),
                    upload_file.content_type.endswith('.png' or '.jpeg')
            )):
                filename = str(uuid.uuid4()) + os.path.splitext(upload_file.name)[
                    -1]
                with open('media/user_tou/' + filename, 'wb') as f:
                    # 分段写入
                    for chunk in upload_file.chunks():
                        f.write(chunk)

                    f.flush()

                return JsonResponse({
                    'code': 200,
                    'msg': '上传文件成功',
                    'file_key': key
                })
            else:
                return JsonResponse({
                    'code': 201,
                    'msg': '图片格式只支持png或jpeg'
                })


def u_img(request, user_id):
    user = UserModel.objects.filter(id=user_id).first()
    img_url = str(user.img1)
    return JsonResponse({
        'code': 200,
        'url': img_url
        })
