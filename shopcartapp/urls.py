from django.urls import path
from shopcartapp.views import LoginView, shop_cart, goods_add, goods_delete
from shopcartapp.views import hot_goods, is_goodsed

app_name = 'shopcartapp'

urlpatterns = [
    path('shopcart/', shop_cart),
    path('hotgood/', hot_goods, name='hot'),
    path('isgoods/', is_goodsed, name='is_goodsed'),
    path('add/', goods_add, name='add_goods'),
    path('delete/', goods_delete, name='goods_delete'),
    path('login/', LoginView.as_view(), name='login'),
]
