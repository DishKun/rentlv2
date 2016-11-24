# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 01:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0009_auto_20161122_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseinfo',
            name='louceng',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='mianji',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='collect',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 22, 9, 1, 6, 111456)),
        ),
        migrations.AlterField(
            model_name='houseinfo',
            name='housetype',
            field=models.CharField(blank=True, choices=[('三室一厅一卫', '三室一厅一卫'), ('三室一厅两卫', '三室一厅两卫'), ('二室一厅一卫', '二室一厅一卫'), ('一室一厅一卫', '一室一厅一卫'), ('四室两厅两卫', '四室两厅两卫'), ('三室两厅两卫', '三室两厅两卫')], max_length=200),
        ),
    ]