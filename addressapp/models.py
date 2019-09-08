from django.db import models


# Create your models here.
class AddressModel(models.Model):
    user_id = models.ForeignKey('indexapp.UserModel',
                                related_name='user',
                                on_delete=models.SET_NULL,
                                verbose_name='用户ID')

    ads = models.CharField(max_length=100,
                           verbose_name='地址')

    name = models.CharField(max_length=20,
                            verbose_name='收件人')

    phone = models.CharField(max_length=11,
                             verbose_name='手机号码')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_address'
        verbose_name_plural = verbose_name = '收货信息'


class DiscountModel(models.Model):
    user_id = models.ForeignKey('indexapp.UserModel',
                                verbose_name='用户ID',
                                related_name='user',
                                on_delete=models.SET_NULL)

    discount_amout = models.FloatField(verbose_name='折扣金额',
                                       default=.8)

    threshold = models.CharField(max_length=100,
                                 verbose_name='满减门槛')

    start_time = models.CharField(max_length=30,
                                  verbose_name='发放时间')

    end_time = models.CharField(max_length=30,
                                verbose_name='结束时间')

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'app_discount'
        verbose_name_plural = verbose_name = '优惠信息'