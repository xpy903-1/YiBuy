from rest_framework import routers


# 声明api路由
from orderapp.orderApi import OrderAPIView

api_router = routers.DefaultRouter()

api_router.register('order', OrderAPIView)
