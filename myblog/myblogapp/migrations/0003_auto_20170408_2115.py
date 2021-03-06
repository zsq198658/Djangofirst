# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 21:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0002_auto_20170408_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 8, 21, 15, 39, 976003), verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='static/image/Art_Image.jpg', upload_to='', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(blank=True, default='static/image/image.jpg', null=True, upload_to='./static/image/', verbose_name='头像'),
        ),
    ]
