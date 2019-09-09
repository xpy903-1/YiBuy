import uuid

from django.db import models


# Create your models here.
class EntertainmentModel(models.Model):
    picture = models.ImageField(verbose_name='图片',
                                upload_to='login/images')
    description = models.TextField(verbose_name='描述',
                                   blank=True)
    time = models.DateTimeField(verbose_name='时间',
                                auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'db_entertainment'
        verbose_name = '吃喝玩乐'
        verbose_name_plural = verbose_name


class CitysModel(models.Model):
    id = models.UUIDField(primary_key=True,
                          verbose_name='城市编号')
    name = models.CharField(max_length=20,
                            verbose_name='城市名称',
                            null=False)
    is_popular = models.BooleanField(verbose_name='是否热门',
                                     choices=((True,'是'),
                                              (False, '否')))
    start_str = models.CharField(max_length=1,
                                 verbose_name='排行名称')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save()

    class Meta:
        db_table = 'db_citys'
        verbose_name = '各大城市'
        verbose_name_plural = verbose_name


class NavigationModel(models.Model):
    img = models.ImageField(verbose_name='导航图片',
                            upload_to='login/images')

    img_name = models.CharField(max_length=20,
                                verbose_name='图片名称')

    img_id = models.ForeignKey('loginapp2.NavigationDetaiModel',
                               verbose_name='图片编号',
                               on_delete=True)

    def __str__(self):
        return self.img_name

    class Meta:
        db_table = 'db_navigation'
        verbose_name = '导航表'
        verbose_name_plural = verbose_name
