from django.contrib import admin
from .models import ShopCarModel, PictureModel


# Register your models here.

# 购物车
class ShopCarAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'good_id', 'count', 'is_selected')  # 显示字段
    fields = ('count', 'is_selected')  # 可更改字段
    ordering = ('id',)  # 按 id 排序


# 商品图片
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture_name', 'picture_path', 'picture_width', 'picture_height')  # 显示字段
    fields = ('picture_name', 'picture_path', 'picture_width', 'picture_height')  # 可更改字段
    ordering = ('id',)  # 按 id 排序


admin.site.register(ShopCarModel, ShopCarAdmin)
admin.site.register(PictureModel, PictureAdmin)
