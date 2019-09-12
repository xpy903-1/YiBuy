from django.urls import path

from .loginapp2API import detaios, change, loginout, u_img, upload_avator

app_name = "loginapp2"





urlpatterns = [

    path('detaios/', detaios, name="detaios"),
    path('change/', change, name="change"),
    path('loginout/', loginout, name="loginout"),
    path('upload/', upload_avator, name="upload"),
    path('imgurl/', u_img, name="u_img"),

]
