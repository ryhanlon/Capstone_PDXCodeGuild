# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20170619_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mediaimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]