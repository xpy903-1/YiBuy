from django.contrib import admin
from .models import NavigationDetaiModel, \
    SelectedModel, CarsouseiMapModel


# Register your models here.
class NavigationDetaiModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_id.picture', 'img_id', 'img_id.picture_name',
                    'goods_id')
    fields = ('img_id.picture', 'img_id.picture_name',)


class CarsouseiMapModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_id.picture', 'img_id', 'img_id.picture_name',
                    'goods_id')
    fields = ('img_id.picture', 'img_id.picture_name',)


class SelectedModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_id.picture', 'img_id', 'img_id.picture_name')
    fields = ('img_id.picture', 'img_id.picture_name',)


admin.site.register(NavigationDetaiModel, NavigationDetaiModelAdmin)
admin.site.register(CarsouseiMapModel, CarsouseiMapModelAdmin)
admin.site.register(SelectedModel, SelectedModelAdmin)
