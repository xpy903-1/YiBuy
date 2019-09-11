from django.urls import path

from .loginapp2API import detaios, change, loginout, u_img, upload_avator

app_name = "loginapp2"

urlpatterns = [

<<<<<<< HEAD
    path('detaios', detaios, name="detaios"),
    path('change', change, name="change"),
    path('loginout', loginout, name="loginout"),
    path('imgurl', img_url, name="img_url"),

    path('detaios/', detaios, name="detaios"),
    path('change/', change, name="change"),
    path('loginout/', loginout, name="loginout"),
    path('imgurl/', img_url, name="img_url"),

=======
    path('detaios/', detaios, name="detaios"),
    path('change/', change, name="change"),
    path('loginout/', loginout, name="loginout"),
    path('upload/', upload_avator, name="upload"),
    path('imgurl/<str:user_id>', u_img, name="u_img"),
>>>>>>> 1b10509d7cad4803c31d6f08f76f43a831cdd792

]
