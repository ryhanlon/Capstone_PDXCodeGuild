# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 21:42
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='Bunny-avatar.gif', upload_to=accounts.models.user_media_upload_handler),
        ),
    ]