# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0019_auto_20161123_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='houseinfo',
            name='housetype',
            field=models.CharField(blank=True, choices=[('三室一厅一卫', '三室一厅一卫'), ('三室一厅两卫', '三室一厅两卫'), ('三室两厅两卫', '三室两厅两卫'), ('四室两厅两卫', '四室两厅两卫'), ('一室一厅一卫', '一室一厅一卫'), ('二室一厅一卫', '二室一厅一卫')], max_length=200),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女'), ('保密', '保密')], default='保密', max_length=10),
        ),
    ]
