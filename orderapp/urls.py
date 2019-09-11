from django.urls import path

from orderapp.views import order_test, order

app_name = 'orderapp'

urlpatterns = [
    # path('type/list/child/<child_id>/<string:id>')
    path('',order)
]
