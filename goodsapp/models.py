from django.db import models

# Create your models here.

class FirstClassify(models.Model):
    name = models.CharField(verbose_name='一级分类名',
                            max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_first_classcify'
        verbose_name_pural = verbose_name = '一级分类表'


class SecondClassify(models.Model):
    name = models.CharField(verbose_name='二级分类名',
                            max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_second_classcify'
        verbose_name_pural = verbose_name = '二级分类表'

class GoodsModel(models.Model):
    goods_img = models.ImageField(verbose_name='商品图片',
                                   upload_to='imags',
                                   width_field='goods_img_width',
                                   height_field='goods_img_height',
                                   null=True,
                                   blank=True)

    goods_img_width = models.IntegerField(verbose_name='宽',
                                           null=True)

    goods_img_height = models.IntegerField(verbose_name='高',
                                            null=True)

    name = models.CharField(verbose_name='水果名',
                            max_length=20)

    goods_price = models.DecimalField(verbose_name='商品价格',
                                   max_digits=10,
                                   decimal_places=2)

    sales_volume = models.IntegerField(verbose_name='销量')

    storage = models.IntegerField(verbose_name='库存')

    market_price = models.DecimalField(verbose_name='市场价格',
                                   max_digits=10,
                                   decimal_places=2)

    produce_place = models.CharField(verbose_name='生产地',
                                     max_length=20)

    detail_img = models.ImageField(verbose_name='详情页图片',
                                   upload_to='imags',
                                   width_field='detail_img_width',
                                   height_field='detail_img_height',
                                   null=True,
                                   blank=True)

    detail_img_width = models.IntegerField(verbose_name='宽',
                                      null=True)

    detail_img_height = models.IntegerField(verbose_name='高',
                                       null=True)

    first_cate_id = models.ForeignKey(FirstClassify,
                                      on_delete=models.CASCADE,
                                      verbose_name='一级分类id')

    second_cate_id = models.ForeignKey(SecondClassify,
                                       on_delete=models.CASCADE,
                                       verbose_name='二级分类id')

    description = models.TextField(verbose_name='商品详情')

    detail = models.TextField(verbose_name='详情')

    is_selected = models.BooleanField(verbose_name='是否精选')

    register_time = models.DateTimeField(verbose_name='注册时间',
                                         auto_now_add=True)

    update_time = models.DateTimeField(verbose_name='更新时间',
                                       auto_now=True)



    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_goods'
        verbose_name_pural = verbose_name = '商品表'









