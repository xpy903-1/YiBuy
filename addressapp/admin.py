from django.contrib import admin

from .models import AddressModel, DiscountModel

# Register your models here.
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'ads ', 'name', 'phone')
    fields = ('user_id', 'ads ', 'name', 'phone')


class DiscountModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'discount_amout', 'threshold', 'start_time', 'end_time')
    fields = ('user_id', 'discount_amout', 'threshold', 'start_time', 'end_time')


admin.site.register(AddressModel, AddressModelAdmin)
admin.site.register(DiscountModel, DiscountModelAdmin)