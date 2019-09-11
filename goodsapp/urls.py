from django.urls import path
from .views import query_goods_info, query_goods_img, goodsclassfiy, adddata,search

app_name = 'goodsapp'



urlpatterns = [
    path('detail/<uid>', query_goods_info),
    path('queryimg/img/uid', query_goods_img),
    path('type/list/<uid>', goodsclassfiy),
    path('search/', search),
    path('adddata', adddata)
]