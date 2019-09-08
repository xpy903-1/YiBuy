from django.contrib import admin
from .models import NavigationDetaiModel, \
    SelectedModel, CarsouseiMapModel


# Register your models here.
class NavigationDetaiModelAdmin(admin.ModelAdmin):
    list_display = ('img', 'img_id', 'img_name', 'goods_id')


class CarsouseiMapModelAdmin(admin.ModelAdmin):
    list_display = ('img', 'img_id', 'img_name', 'goods_id')


class SelectedModelAdmin(admin.ModelAdmin):
    list_display = ('img', 'img_id', 'img_name')


admin.site.register(NavigationDetaiModel, NavigationDetaiModelAdmin)
admin.site.register(CarsouseiMapModel, CarsouseiMapModelAdmin)
admin.site.register(SelectedModel, SelectedModelAdmin)
