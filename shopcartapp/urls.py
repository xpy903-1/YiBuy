from django.urls import path
from shopcartapp.views import new_goods, LoginView, car_goods
app_name = 'shopcartapp'


urlpatterns = [
    path('newgoods/', new_goods),
    path('cargoods/', car_goods),
    path('login/',LoginView.as_view(), name='login'),
]