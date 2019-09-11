from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from addressapp.models import AddressModel
from indexapp.models import UserModel


@csrf_exempt  # 跨域请求
def address_query(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        if not any((name, phone)):
            return JsonResponse({
                'code': 201,
                'msg': '请输入至少一个查询条件'
            })
        else:
            if name:
                user = UserModel.objects.filter(name=name).first()
                address = user.address.all()
                data = []
                for i in address:
                    d = {
                        'ads': i.ads,
                        'name': i.name,
                        'phone': i.phone
                    }
                    data.append(d)
                return JsonResponse({
                    'code': 200,
                    'msg': 'ok',
                    'data': data
                })
            else:
                user = UserModel.objects.filter(phone=phone).first()
                address = user.address.all()
                data = []
                for i in address:
                    d = {
                        'ads': i.ads,
                        'name': i.name,
                        'phone': i.phone
                    }
                    data.append(d)
                return JsonResponse({
                    'code': 200,
                    'msg': 'ok',
                    'data': data
                })
    else:
        return render(request, 'adsquery.html')

@csrf_exempt
def address_add(request):
    if request.method == 'POST':
        user_id = UserModel.objects.get(pk=request.POST.get('user_id', None))
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        ads = request.POST.get('ads', None)
        if not all((user_id, name, phone, ads)):
            return JsonResponse({
                'code': 400,
                'msg': '请求的参数不完整'
            })
        add_data = AddressModel()
        add_data.user_id = user_id
        add_data.name = name
        add_data.phone = phone
        add_data.ads = ads
        add_data.save()
        return JsonResponse({
            'code': 200,
            'msg': '添加地址成功',
            'data': {
                'user':add_data.user_id.name,
                'name':add_data.name,
                'phone':add_data.phone,
                'ads':add_data.ads
            }
        })
    else:
        return render(request, 'adsadd.html')


def address_edit(request):
    if request.method == 'POST':
        user_id = UserModel.objects.get(pk=request.POST.get('user_id', None))
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        ads = request.POST.get('ads', None)
        if not all((user_id, name, phone, ads)):
            return JsonResponse({
                'code': 400,
                'msg': '请求的参数不完整'
            })
        name= AddressModel.objects.get('name',None)
    else:
        return render(request, 'adsedit.html')


def address_delete(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'adsdelete.html')
