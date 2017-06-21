# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookmedia',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookmedia',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bookmedia',
            name='type',
            field=models.CharField(choices=[('BPG', 'book pages'), ('GPG', 'game pages'), ('DPG', 'dashboard pages')], max_length=3),
        ),
    ]
