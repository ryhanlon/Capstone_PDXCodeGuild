# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 20:50
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merit',
            name='image',
            field=models.ImageField(upload_to=accounts.models.user_media_upload_handler),
        ),
    ]
