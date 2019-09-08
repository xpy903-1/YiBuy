from django.contrib import admin
from .models import ShopCarModel, PictureModel
# Register your models here.

class ShopCarAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'good_id', 'count', 'is_selected')

class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture_name', 'picture_path')


admin.site.register(ShopCarModel, ShopCarAdmin)
admin.site.register(PictureModel, PictureAdmin)
