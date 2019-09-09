from django.contrib import admin

# Register your models here.
from goodsapp.models import FirstClassify, SecondClassify, GoodsModel


class FirstClassifyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class SecondClassifyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class GoodsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'goods_img', 'goods_img_width', 'goods_img_height',
                    'name', 'goods_price','sales_volume', 'storage', 'market_price',
                    'produce_place',' detail_img', 'detail_img_width', 'detail_img_height',
                    'first_cate_id', 'second_cate_id', 'description', 'detail', 'is_selected',
                    'register_time', 'update_time')

    fields = ('id', 'goods_img',
                    'name', 'goods_price','sales_volume', 'storage', 'market_price',
                    'produce_place',' detail_img',
                    'first_cate_id', 'second_cate_id', 'description', 'detail', 'is_selected',
                    'register_time', 'update_time')


admin.site.register(FirstClassify, FirstClassifyAdmin)
admin.site.register(SecondClassify, SecondClassifyAdmin)
admin.site.register(GoodsModel, GoodsModelAdmin)
