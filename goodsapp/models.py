import uuid

from django.db import models

# Create your models here.


class FirstClassify(models.Model):
    uid = models.UUIDField(primary_key=True,
                             verbose_name='一级分类id')


    name = models.CharField(verbose_name='一级分类名',
                            max_length=20)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # self.uid1 = uuid.uuid4().hex
        if not self.uid:
            self.uid = uuid.uuid4().hex

        super().save()

    class Meta:
        db_table = 't_first_classcify'
        verbose_name_plural = verbose_name = '一级分类表'


class SecClassify(models.Model):
    uid1 = models.UUIDField(primary_key=True,
                             verbose_name='二级分类id')

    uid2 = models.ForeignKey(FirstClassify,
                             verbose_name='所属一级分类',
                             on_delete=models.CASCADE,
                             )

    name = models.CharField(verbose_name='二级分类名',
                             max_length=20)

    def __str__(self):
        return str(self.uid2)



    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if not self.uid1:

            self.uid1 = uuid.uuid4().hex

        super().save()

    class Meta:
        db_table = 't_sec_classcify'
        verbose_name_plural = verbose_name = '二级分类表'



class GoodsModel(models.Model):
    uid = models.UUIDField(verbose_name='水果id',
                           primary_key=True)

    goods_img = models.CharField(verbose_name='商品图片',
                                   max_length=200,
                                   null=True,
                                   )



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

    detail_img = models.CharField(verbose_name='详情页图片',
                                   max_length=200,
                                   null=True,
                                   )



    cate_id = models.ForeignKey(SecClassify,
                                      on_delete=models.CASCADE,
                                      verbose_name='分类id')



    description = models.TextField(verbose_name='商品详情')

    detail = models.TextField(verbose_name='详情')

    is_selected = models.BooleanField(verbose_name='是否精选')

    register_time = models.DateTimeField(verbose_name='注册时间',
                                         auto_now_add=True)

    update_time = models.DateTimeField(verbose_name='更新时间',
                                       auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.uid:
            self.uid = uuid.uuid4().hex

        super().save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_goods'
        verbose_name_plural = verbose_name = '商品表'









