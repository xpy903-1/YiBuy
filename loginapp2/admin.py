from django.contrib import admin
from .models import NavigationDetaiModel, \
    SelectedModel, CarsouseiMapModel


# Register your models here.
class NavigationDetaiModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_id', 'goods_id', 'img_name', 'img', 'img_height',
                    'img_width')
    fields = ('img_id', 'goods_id', 'img_name', 'img', 'img_height', 'img_width')


class CarsouseiMapModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_id', 'goods_id', 'img_name', 'img', 'img_height',
                    'img_width')
<<<<<<< HEAD
    fields = ('img_id', 'goods_id', 'img_name', 'img', 'img_height',
              'img_width')
=======
    fields = ('img_id', 'goods_id', 'img_name', 'img', 'img_height', 'img_width')
>>>>>>> 6920fef5b34096cb11c1d0b52060181f5d95e671


class SelectedModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_id', 'img_name', 'img', 'img_height',
                    'img_width')
    fields = ('img_id',  'img_name', 'img', 'img_height', 'img_width')


admin.site.register(NavigationDetaiModel, NavigationDetaiModelAdmin)
admin.site.register(CarsouseiMapModel, CarsouseiMapModelAdmin)
admin.site.register(SelectedModel, SelectedModelAdmin)
