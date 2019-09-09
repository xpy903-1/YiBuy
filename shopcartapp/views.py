from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from indexapp.models import UserModel


class LoginView(View):
    # get 方式返回登录界面
    def get(self, request):
        return render(request, 'login.html')

    # post 验证用户密码是否正确
    def post(self, request):
        error_msg = '用户名输入错误'
        error_pwd = '密码输入错误'
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)

        if all((name, password)):
            user_name = UserModel.objects.filter(name=name)
            # 判断用户名是否存在
            if user_name.exists():
                user = user_name.first()
                if check_password(password, user.auth_key):
                    request.session['login_user'] = {
                        'id': user.id,
                        'name': user.name
                    }
                    return redirect('/')
            else:
                error_msg = '用户名不存在，请先注册'
        return render(request, 'login.html', locals())