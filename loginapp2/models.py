from django.db import models


# Create your models here.
# 创建一个抽象模型类
class BaseModel(models.Model):
    img = models.ImageField(verbose_name="图片",
                            upload_to="loginapp2")
    img_id = models.CharField(max_length=20,
                              verbose_name="图片ID")
    img_name = models.CharField(max_length=100,
                                verbose_name="图片名称")

    class Meta:
        abstract = True


class NavigationDetaiModel(BaseModel):
    goods_id = models.ForeignKey('goodsapp.models.GoodsModel',
                                 verbose_name="商品ID")

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
    goods_id = models.ForeignKey("goodsapp.models.GoodsModel",
                                 verbose_name="商品ID")

    def __str__(self):
        return self.img_name

    class Meta:
        db_table = "app_carsouseimap"
        verbose_name_plural = verbose_name = "轮播图表"
