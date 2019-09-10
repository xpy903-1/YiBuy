from django.urls import path
from .views import query_goods_info, query_goods_img, goodsclassfiy, adddata

app_name = 'goodsapp'



urlpatterns = [
    path('queryinfo', query_goods_info),
    path('queryimg', query_goods_img),
    path('goodsclassfiy', goodsclassfiy),
    path('adddata', adddata)
]