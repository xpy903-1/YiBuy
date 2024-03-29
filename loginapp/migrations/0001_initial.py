# Generated by Django 2.0.1 on 2019-09-10 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginapp2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitysModel',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='城市编号')),
                ('name', models.CharField(max_length=20, verbose_name='城市名称')),
                ('is_popular', models.BooleanField(choices=[(True, '是'), (False, '否')], verbose_name='是否热门')),
                ('start_str', models.CharField(max_length=1, verbose_name='排行名称')),
            ],
            options={
                'verbose_name': '各大城市',
                'verbose_name_plural': '各大城市',
                'db_table': 'db_citys',
            },
        ),
        migrations.CreateModel(
            name='EntertainmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(height_field='pic_height', upload_to='login/images', verbose_name='图片', width_field='pic_width')),
                ('pic_width', models.IntegerField(null=True, verbose_name='图片宽')),
                ('pic_height', models.IntegerField(null=True, verbose_name='图片高')),
                ('description', models.TextField(blank=True, verbose_name='描述')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '吃喝玩乐',
                'verbose_name_plural': '吃喝玩乐',
                'db_table': 'db_entertainment',
            },
        ),
        migrations.CreateModel(
            name='NavigationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=20, verbose_name='图片名称')),
                ('img_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginapp2.NavigationDetaiModel', verbose_name='图片编号')),
            ],
            options={
                'verbose_name': '导航表',
                'verbose_name_plural': '导航表',
                'db_table': 'db_navigation',
            },
        ),
    ]
