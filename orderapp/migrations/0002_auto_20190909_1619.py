# Generated by Django 2.0.1 on 2019-09-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='下单时间'),
        ),
    ]
