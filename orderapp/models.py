import uuid

from django.db import models


# Create your models here.
from addressapp.models import AddressModel
from goodsapp.models import GoodsModel
from indexapp.models import UserModel


class OrderModel(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey(UserModel,
                                verbose_name='用户ID',
                                on_delete=models.CASCADE)

    total = models.FloatField(verbose_name='总价格')

    time = models.DateTimeField(auto_now=True,
                                verbose_name='下单时间')

    address_id = models.ForeignKey(AddressModel,
                                   verbose_name='地址ID',
                                   on_delete=models.CASCADE)

    order_status = models.IntegerField(verbose_name='订单状态',
                                       choices=((1, '已下单'),
                                                (2, '已支付'),
                                                (3, '已发货'),
                                                (4, '已收货'),
                                                (5, '已完成'),
                                                (0, '已取消')))

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.id = uuid.uuid4().hex
        super().save()

    class Meta:
        db_table = 'app_order'
        verbose_name_plural = verbose_name = '订单列表'


class OrderDetailModel(models.Model):
    id = models.UUIDField(primary_key=True)
    order_id = models.ForeignKey(OrderModel,
                                 verbose_name='订单ID',
                                 on_delete=models.CASCADE)

    goods_id = models.ForeignKey(GoodsModel,
                                 verbose_name='商品ID',
                                 on_delete=models.CASCADE)

    count = models.IntegerField(verbose_name='商品数量')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.id = uuid.uuid4().hex
        super().save()

    class Meta:
        db_table = 'app_orderdetail'
        verbose_name_plural = verbose_name = '订单详情'
