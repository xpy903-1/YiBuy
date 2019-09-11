from django.urls import path

from .views import check_phone, login_pwd


app_name = 'loginapp'

urlpatterns = [
     path('check/', check_phone, name='check'),
     path('login/', login_pwd, name='login')
]

