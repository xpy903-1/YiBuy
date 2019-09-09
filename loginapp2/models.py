import uuid

from django.db import models


# Create your models here.
# 创建一个抽象模型类
from goodsapp.models import GoodsModel
from shopcartapp.models import PictureModel


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True)
    img_id = models.ForeignKey(PictureModel,
                               on_delete=models.CASCADE)


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.id:
            self.id = uuid.uuid4().hex


    class Meta:
        abstract = True


class NavigationDetaiModel(BaseModel):
    goods_id = models.ForeignKey(GoodsModel,
                                 verbose_name="商品ID",
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.img_id.picture_name

    class Meta:
        db_table = "app_navigationdetai"
        verbose_name = verbose_name_plural = "导航详情表"


class SelectedModel(BaseModel):

    def __str__(self):
        return self.img_id.picture_name

    class Meta:
        db_table = "app_selected"
        verbose_name = verbose_name_plural = "精选推荐表"


class CarsouseiMapModel(BaseModel):

    goods_id = models.ForeignKey(GoodsModel,
                                 verbose_name="商品ID",
                                 on_delete=True)

    def __str__(self):
        return self.img_id.picture_name

    class Meta:
        db_table = "app_carsouseimap"
        verbose_name_plural = verbose_name = "轮播图表"
