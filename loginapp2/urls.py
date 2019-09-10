from django.urls import path

from .views import detaios, change, loginout, img_url1
app_name = "loginapp2"

urlpatterns = [

    path('detaios/', detaios, name="detaios"),
    path('change/', change, name="change"),
    path('loginout/', loginout, name="loginout"),
    path('upload/', img_url1, name="upload"),
    path('imgurl/<string:key>', img_url1, name="img_url"),



]