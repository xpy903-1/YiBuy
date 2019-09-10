from django.urls import path

from .views import detaios, change, loginout, img_url
app_name = "loginapp2"

urlpatterns = [
<<<<<<< Updated upstream
    path('detaios', detaios, name="detaios"),
    path('change', change, name="change"),
    path('loginout', loginout, name="loginout"),
    path('imgurl', img_url, name="img_url"),
=======
    path('detaios/', detaios, name="detaios"),
    path('change/', change, name="change"),
    path('loginout/', loginout, name="loginout"),
    path('imgurl/', img_url, name="img_url"),
>>>>>>> Stashed changes

]