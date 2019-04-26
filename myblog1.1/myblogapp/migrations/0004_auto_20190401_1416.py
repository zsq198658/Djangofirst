# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0003_auto_20190325_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default=b'static/image/Art_Image.jpg', height_field=100, upload_to=b'static/image/article_image/%Y/%m/%d', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', width_field=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(blank=True, default=b'static/image/image.jpg', height_field=100, null=True, upload_to=b'static/image/user_logo/%Y/%m/%d', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', width_field=100),
        ),
    ]
