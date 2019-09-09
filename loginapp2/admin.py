from django.contrib import admin
from .models import NavigationDetaiModel, \
    SelectedModel, CarsouseiMapModel


# Register your models here.
class NavigationDetaiModelAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'img_id', 'goods_id', 'img_name', 'img1', 'img_height',
    'img_width')
    fields = (
    'img_id', 'goods_id', 'img_name', 'img1', 'img_height', 'img_width')


class CarsouseiMapModelAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'img_id', 'goods_id', 'img_name', 'img1', 'img_height',
    'img_width')
    fields = ('img_id', 'goods_id', 'img_name', 'img1', 'img_height',
              'img_width')


class SelectedModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_id', 'img_name', 'img1', 'img_height',
                    'img_width')
    fields = ('img_id', 'img_name', 'img1', 'img_height', 'img_width')


admin.site.register(NavigationDetaiModel, NavigationDetaiModelAdmin)
admin.site.register(CarsouseiMapModel, CarsouseiMapModelAdmin)
admin.site.register(SelectedModel, SelectedModelAdmin)
