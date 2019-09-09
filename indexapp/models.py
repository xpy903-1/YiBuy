import uuid

from django.db import models
from goodsapp.models import GoodsModel


# Create your models here.


class UserModel(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='电话')
    pwd = models.CharField(max_length=100, verbose_name='密码')
    sex = models.CharField(max_length=10, verbose_name='性别',
                           choices=(('male', '男'), ('female', '女')), default='male')
    number = models.CharField(max_length=18, verbose_name='身份证号')
    img1 = models.ImageField(verbose_name='用户图像', upload_to='users',
                             width_field='users_img_width',
                             height_field='users_img_height',
                             null=True,
                             blank=True
                             )
    money = models.DecimalField(verbose_name='余额', default=0.00, max_digits=10, decimal_places=2)
    level = models.IntegerField(verbose_name='用户级别',
                                choices=((0, '青铜'), (1, '白银'), (2, '黄金')), default=0)
    is_life = models.BooleanField(verbose_name='是否激活', default=False)
    is_rm = models.BooleanField(verbose_name='是否删除', default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_user'
        verbose_name_plural = verbose_name = '用户列表'


class UserCommentModel(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey(UserModel, verbose_name='用户ID', on_delete=models.CASCADE)
    goods_id = models.ForeignKey('GoodsModel', on_delete=models.CASCADE, verbose_name='商品ID')
    detail = models.CharField(max_length=500, verbose_name='评论详情')
    time = models.DateTimeField(verbose_name='评论时间')

    def __str__(self):
        return self.detail

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save()

    class Meta:
        db_table = 'app_user_detail'
        verbose_name_plural = verbose_name = '用户评论'


class ViceCommentModel(models.Model):
    id = models.UUIDField(primary_key=True)
    comment_id = models.ForeignKey(UserCommentModel, Cverbose_name='评论ID', on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, verbose_name='评论内容')

    def __str__(self):
        return self.comment

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save()

    class Meta:
        db_table = 'app_user_detail_fu'
        verbose_name_plural = verbose_name = '用户评论副表'
