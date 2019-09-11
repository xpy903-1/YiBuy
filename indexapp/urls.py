from django.urls import path
from indexapp.indexApi import navigation, eats, member_show, page_welfare, home_page
app_name = 'indexapp'

urlpatterns = [
    path('index/', home_page, name='page'),
    path('nav/', navigation, name='nav'),
    path('eat/', eats, name='eat'),
    path('card/', member_show, name='show'),
    path('welfare/', page_welfare, name='welfare'),

]