from django.db import models

# Create your models here.
class ShopCarModel(models.Model):
    user_id = models.ForeignKey('indexapp.UserModel',
                                on_delete=models.CASCADE,
                                verbose_name="用户ID")

    good_id = models.ForeignKey('goodsapp.GoodsModel',
                                on_delete=models.CASCADE,
                                verbose_name="商品ID")

    count = models.IntegerField(verbose_name='数量',
                                default=0)

    is_selected = models.BooleanField(verbose_name='是否选中',
                                      default=False)

    def __str__(self):
        return self.user_id + "-" + self.good_id

    class Meta:
        db_table = 'car_table'
        verbose_name_plural = "购物车"

class PictureModel(models.Model):
    picture_name = models.CharField(max_length=30,
                                    verbose_name='图片名称')

    picture_path = models.ImageField(verbose_name='商品图片',
                                     upload_to='picture')

    def __str__(self):
        return self.picture_name

    class Meta:
        db_table = 'picture_table'
        verbose_name_plural = "图片表"
