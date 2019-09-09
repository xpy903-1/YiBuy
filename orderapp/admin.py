from django.contrib import admin

# Register your models here.
from orderapp.models import OrderModel, OrderDetailModel


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'total', 'time', 'address_id', 'order_status']
    fields = ['user_id', 'total', 'time', 'address_id', 'order_status']


class OrderDetailModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'goods_id', 'count']
    fields = ['order_id', 'goods_id', 'count']


admin.site.register(OrderModel, OrderModelAdmin)
admin.site.register(OrderDetailModel, OrderDetailModelAdmin)
