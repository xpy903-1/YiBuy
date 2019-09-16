import json
import os
import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt


from indexapp.models import UserModel
from signal import login_yz


@csrf_exempt
def detaios(request):
    if request.method == "POST":
        token = json.loads(request.body)
        print(token)
        user_id = token.get('user_id')
        print(user_id)
        if not user_id:
            return JsonResponse({
                'code': 300,
                'msg': "用户未登录,请重新登录"
    })
        else:
            user = UserModel.objects.filter(id=user_id)
            print(user)
            if user.exists():
                user = user.first()

                return JsonResponse({
                        'code': 200,
                        'msg': '获取成功',
                        'name': user.name,
                        'gender': user.sex,
                        'level': user.level,
                })
            else:
                return JsonResponse({
                                        'code': 300,
                                        'msg': '该用户不存在', })


@csrf_exempt
def change(request):
    if request.method == "POST":
        date = json.loads(request.body)
        print(date)
        user_name = date.get('user_name', None)
        user_phone = date.get('user_phone', None)
        user_pwd = date.get('user_pwd', None)
        user_id = date.get('user_id')
        if not user_id:
            return JsonResponse({
                'code': 300,
                'msg': "用户未登录,请重新登录"
            })
        if not all((user_name, user_pwd, user_phone)):
            return JsonResponse({
                    'code': 300,
                    'msg': '数据不能为空'
                })
        user = UserModel.objects.filter(id=user_id).first()
        if user:
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
    user_id = login_yz.send(sender='ap', request=request)[0][1]
    if not user_id:
        return JsonResponse({
            'code': 300,
            'msg': "用户未登录,请重新登录"
        })
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
    user_id = login_yz.send(sender='ap', request=request)[0][1]
    if not user_id:
        return JsonResponse({
            'code': 300,
            'msg': "用户未登录,请重新登录"
        })
    if request.method == "POST":
        user = UserModel.objects.filter(id=user_id).first()
        key = user.name
        upload_file: InMemoryUploadedFile = request.FILES.get('img1')
        print(upload_file)
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
    else:
        return JsonResponse({
            'code': 300,
            'msg': '图片'
        })

def u_img(request):
    user_id = login_yz.send(sender='ap', request=request)[0][1]
    if not user_id:
        return JsonResponse({
            'code': 300,
            'msg': "用户未登录,请重新登录"
        })
    user = UserModel.objects.filter(id=user_id).first()
    img_url = 'http://127.0.0.1:8000/m/' + str(user.img1)
    return JsonResponse({
        'code': 200,
        'url': img_url
        })
