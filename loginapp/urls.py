from django.urls import path
from .views import msg_code, check_phone, login_pwd, msg_login, forgot

app_name = 'loginapp'

urlpatterns = [
     # path('add', add_city),
     path('msgcode/', msg_code, name='msgcode'),
     path('check/', check_phone, name='check'),
     path('login/', login_pwd, name='login'),
     path('msglogin/', msg_login, name='msglogin'),
     path('forgot/', forgot, msg='forgot')
]

