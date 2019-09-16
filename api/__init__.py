from rest_framework import routers

# 声明api路由
from orderapp.orderApi import OrderAPIView
from shopcartapp.shopcartapi import GoodsAPIView

api_router = routers.DefaultRouter()

api_router.register('order', OrderAPIView)
api_router.register('shopcart', GoodsAPIView)
