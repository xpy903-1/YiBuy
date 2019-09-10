from django.contrib import admin

# Register your models here.
from goodsapp.models import FirstClassify, SecClassify, GoodsModel


class FirstClassifyAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name')
    fields = ('name',)

class SecClassifyAdmin(admin.ModelAdmin):
    list_display = ('uid1', 'uid2', 'name', 'img')
    fields = ('name', 'uid2', 'img')

class GoodsModelAdmin(admin.ModelAdmin):
    list_display = ('uid', 'goods_img',
                    'name', 'goods_price','sales_volume', 'storage', 'market_price',
                    'produce_place','detail_img','cate_id',
                    'description', 'detail', 'is_selected','register_time', 'update_time'
                    )

    fields = ('goods_img',
                    'name', 'goods_price','sales_volume', 'storage', 'market_price',
                    'produce_place', 'detail_img','cate_id',
                     'description', 'detail', 'is_selected',
                    )



admin.site.register(FirstClassify, FirstClassifyAdmin)
admin.site.register(SecClassify, SecClassifyAdmin)
admin.site.register(GoodsModel, GoodsModelAdmin)
