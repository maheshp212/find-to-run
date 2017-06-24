# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find2run', '0002_auto_20170624_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lattitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]