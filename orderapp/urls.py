from django.urls import path

from orderapp.views import order_test, order, daohang, feilei

app_name = 'orderapp'

urlpatterns = [
    path('list/<child_id>/<id>', daohang),
    path('home/<category_id>', feilei),
    path('', order),
    path('t', order_test)
]
