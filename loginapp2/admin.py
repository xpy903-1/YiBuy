from django.contrib import admin
from .models import NavigationDetaiModel, \
    SelectedModel, CarsouseiMapModel


# Register your models here.
class NavigationDetaiModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_id', 'goods_id')
    fields = ('img_id',)


class CarsouseiMapModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_id', 'img_id', 'img_id',
                    'goods_id')
    fields = ('img_id',)


class SelectedModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_id')
    fields = ('img_id',)


admin.site.register(NavigationDetaiModel, NavigationDetaiModelAdmin)
admin.site.register(CarsouseiMapModel, CarsouseiMapModelAdmin)
admin.site.register(SelectedModel, SelectedModelAdmin)
