from django.contrib import admin

# Register your models here.
from orderapp.models import OrderModel


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'total', 'time', 'address_id', 'order_status', 'goods_id', 'count']
    fields = ['user_id','address_id', 'order_status', 'good_id', 'count']


admin.site.register(OrderModel, OrderModelAdmin)
