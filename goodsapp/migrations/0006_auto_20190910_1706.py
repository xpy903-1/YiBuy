# Generated by Django 2.0.1 on 2019-09-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodsapp', '0005_auto_20190910_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secclassify',
            name='img',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='商品图片'),
        ),
    ]