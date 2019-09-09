from django.contrib import admin

# Register your models here.
from goodsapp.models import FirstClassify, SecClassify, GoodsModel


class FirstClassifyAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name')
    fields = ('name',)

class SecClassifyAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name')
    fields = ('name', 'uid')

class GoodsModelAdmin(admin.ModelAdmin):
    list_display = ('uid', 'goods_img', 'goods_img_width', 'goods_img_height',
                    'name', 'goods_price','sales_volume', 'storage', 'market_price',
                    'produce_place','detail_img', 'detail_img_width', 'detail_img_height',
                    'cate_id', 'description', 'detail', 'is_selected','register_time', 'update_time'
                    )

    fields = ('goods_img',
                    'name', 'goods_price','sales_volume', 'storage', 'market_price',
                    'produce_place', 'detail_img',
                    'cate_id', 'description', 'detail', 'is_selected',
                    )



admin.site.register(FirstClassify, FirstClassifyAdmin)
admin.site.register(SecClassify, SecClassifyAdmin)
admin.site.register(GoodsModel, GoodsModelAdmin)
