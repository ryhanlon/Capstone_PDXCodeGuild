# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0002_auto_20170706_2306'),
        ('accounts', '0002_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='merits',
            field=models.ManyToManyField(blank=True, through='insights.Awardance', to='insights.Merit'),
        ),
    ]