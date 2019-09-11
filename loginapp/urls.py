from django.urls import path
from .views import add_city, msg_code, check_phone, login_pwd, msg_login, forgot

app_name = 'loginapp'

urlpatterns = [
     path('add', add_city),
     path('msg_', msg_code),
     path('check', check_phone),
     path('login', login_pwd),
     path('msg', msg_login),
     path('forgot', forgot)
]

