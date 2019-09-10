from django.urls import path
from indexapp.indexApi import index, eats, member_show, page_welfare, home_page
app_name = 'indexapp'

urlpatterns = [
    path('nav/<category_id>', index, name='nav'),
    path('eat/', eats, name='eat'),
    path('show/', member_show, name='show'),
    path('welfare/', page_welfare, name='welfare'),
    path('page/', home_page, name='page'),
]