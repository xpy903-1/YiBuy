from django.db import models

# Create your models here.
class OrderModel(models.Model):
    user_id = models.ForeignKey('indexapp.models.UserModel',
                                verbose_name='用户ID')

    total = models.FloatField(verbose_name='总价格')

    time = models.DateTimeField(auto_now=True,
                                verbose_name='下单时间')

    address_id = models.ForeignKey('addressapp.models.addressModel',
                                     verbose_name='地址ID')

    order_status = models.IntegerField(verbose_name='订单状态',
                                      choices=((1, '已下单'),
                                               (2, '已支付'),
                                               (3, '已发货'),
                                               (4, '已收货'),
                                               (5, '已完成'),
                                               (0, '已取消')))
    class Meta:
        db_table = 'app_order'
        verbose_name_plural = verbose_name = '订单列表'


class OrderDetailModel(models.Model):
    order_id = models.ForeignKey(OrderModel,
                                 verbose_name='订单ID',
                                 on_delete=models.CASCADE)

    goods_id = models.ForeignKey('goodsapp.models.GoodsModel',
                                 verbose_name='商品ID',
                                 on_delete=models.CASCADE)

    count = models.IntegerField(verbose_name='商品数量')
    class Meta:
        db_table = 'app_orderdetail'
        verbose_name_plural = verbose_name = '订单详情'
