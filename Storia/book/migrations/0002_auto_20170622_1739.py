# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 17:39
from __future__ import unicode_literals

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='copyright',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='reading_level',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='word_count',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='bookmedia',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=book.models.media_upload_handler),
        ),
        migrations.AlterField(
            model_name='bookmedia',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=book.models.media_upload_handler),
        ),
    ]
