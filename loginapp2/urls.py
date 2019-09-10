from django.urls import path

from .views import detaios, change, loginout, img_url1,upload_avator
app_name = "loginapp2"

urlpatterns = [

    path('detaios/', detaios, name="detaios"),
    path('change/', change, name="change"),
    path('loginout/', loginout, name="loginout"),
    path('upload/', upload_avator, name="upload"),
    path('imgurl/<key>', img_url1, name="img_url"),



]