import uuid

from django.db import models

# Create your models here.
# 创建一个抽象模型类
from goodsapp.models import GoodsModel
from loginapp.models import NavigationModel
from shopcartapp.models import PictureModel


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True)
    img_id = models.ForeignKey(PictureModel,
                               on_delete=models.CASCADE)
    img_name = models.CharField(max_length=50,
                                verbose_name="图片名")
    img1 = models.ImageField(verbose_name="图片",
                             upload_to='loginapp2',
                             width_field='img_width',
                             height_field='img_height'
                             )
    # 图片宽度
    img_width = models.IntegerField(verbose_name='商品图片宽度',
                                    null=True)

    # 图片高度
    img_height = models.IntegerField(verbose_name='商品图片高度',
                                     null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save()

    class Meta:
        abstract = True


class NavigationDetaiModel(BaseModel):
    goods_id = models.ForeignKey(GoodsModel,
                                 related_name="goods",
                                 verbose_name="商品ID",
                                 on_delete=models.CASCADE)
    nav_id = models.ForeignKey(NavigationModel,
                               related_name="navs",
                               verbose_name="导航ID",
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.img_name

    class Meta:
        db_table = "app_navigationdetai"
        verbose_name = verbose_name_plural = "导航详情表"


class SelectedModel(BaseModel):

    def __str__(self):
        return self.img_name

    class Meta:
        db_table = "app_selected"
        verbose_name = verbose_name_plural = "精选推荐表"


class CarsouseiMapModel(BaseModel):
    goods_id = models.ForeignKey(GoodsModel,
                                 verbose_name="商品ID",
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.img_name

    class Meta:
        db_table = "app_carsouseimap"
        verbose_name_plural = verbose_name = "轮播图表"
