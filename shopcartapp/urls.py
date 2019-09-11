from django.urls import path
from shopcartapp.views import LoginView,  shop_cart, goods_api #add_shopcart
from shopcartapp.views import hot_goods, is_goodsed

app_name = 'shopcartapp'


urlpatterns = [
    path('shopcart/', shop_cart),
    # path('api/', goods_api.as_view(), name='api'),
    path('hotgood/', hot_goods, name='hot'),
    path('isgoods/', is_goodsed, name='is_goodsed'),
    path('login/', LoginView.as_view(), name='login'),
    # path('car/<id>', add_shopcart, name='shopcart'),
]