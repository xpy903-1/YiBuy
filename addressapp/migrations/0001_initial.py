# Generated by Django 2.0.1 on 2019-09-10 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('indexapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='地址编号')),
                ('ads', models.CharField(max_length=100, verbose_name='地址')),
                ('name', models.CharField(max_length=20, verbose_name='收件人')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号码')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='indexapp.UserModel', verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '收货信息',
                'verbose_name_plural': '收货信息',
                'db_table': 'app_address',
            },
        ),
        migrations.CreateModel(
            name='DiscountModel',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='优惠活动编号')),
                ('discount_amout', models.FloatField(default=0.8, verbose_name='折扣金额')),
                ('threshold', models.CharField(max_length=100, verbose_name='满减门槛')),
                ('start_time', models.CharField(max_length=30, verbose_name='发放时间')),
                ('end_time', models.CharField(max_length=30, verbose_name='结束时间')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='indexapp.UserModel', verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '优惠信息',
                'verbose_name_plural': '优惠信息',
                'db_table': 'app_discount',
            },
        ),
    ]
