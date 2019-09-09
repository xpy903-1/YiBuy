import uuid

from django.db import models


# Create your models here.
# 购物车模板
class ShopCarModel(models.Model):
    # 主键 ID
    id = models.UUIDField(primary_key=True,
                          verbose_name='购物车编号')

    # 用户 ID
    user_id = models.ForeignKey('indexapp.UserModel',
                                on_delete=models.CASCADE,
                                verbose_name="用户ID")

    # 购物车 ID
    good_id = models.ForeignKey('goodsapp.GoodsModel',
                                on_delete=models.CASCADE,
                                verbose_name="商品ID")

    # 商品数量
    count = models.IntegerField(verbose_name='数量',
                                default=1)

    # 是否选中上品
    is_selected = models.BooleanField(verbose_name='是否选中',
                                      default=True)  # 默认选中

    def __str__(self):
        return self.user_id + "-" + self.good_id

    # 主键 ID 设置为 uuid
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save()

    class Meta:
        db_table = 'car_table'  # 表名
        verbose_name_plural = "购物车"  # 清除复数中文名


# 商品图片模板
class PictureModel(models.Model):
    # 主键 ID
    id = models.UUIDField(primary_key=True,
                          verbose_name='图片编号')

    # 商品图片名称
    picture_name = models.CharField(max_length=30,
                                    verbose_name='图片名称')

    # 商品图片
    picture_path = models.ImageField(verbose_name='商品图片',
                                     upload_to='picture')

    # 主键 ID 设置为 UUID
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save()

    def __str__(self):
        return self.picture_name

    class Meta:
        db_table = 'picture_table'  # 表名
        verbose_name_plural = "图片表"  # 清除复数中文名
