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
    id = models.CharField(primary_key=True,
                          max_length=5,
                          verbose_name='城市编号',
                          unique=True)
    name = models.CharField(max_length=20,
                            verbose_name='城市名称',
                            null=False)
    is_popular = models.BooleanField(verbose_name='是否热门',
                                     choices=((True,'是'),
                                              (False, '否')))
    start_str = models.CharField(max_length=20,
                                 verbose_name='排行名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'db_citys'
        verbose_name = '各大城市'
        verbose_name_plural = verbose_name


class NavigationModel(models.Model):
    img = models.ImageField(verbose_name='导航图片',
                            upload_to='login/images')

    img_name = models.CharField(max_length=20,
                                verbose_name='图片名称')

    img_id = models.CharField(verbose_name='图片编号',
                              max_length=5)

    def __str__(self):
        return self.img_name

    class Meta:
        db_table = 'db_navigation'
        verbose_name = '导航表'
        verbose_name_plural = verbose_name
