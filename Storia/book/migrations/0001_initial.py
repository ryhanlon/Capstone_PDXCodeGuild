# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 18:30
from __future__ import unicode_literals

import book.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visual_artist', models.CharField(max_length=256)),
                ('animator', models.CharField(blank=True, max_length=256, null=True)),
                ('composer', models.CharField(blank=True, max_length=256, null=True)),
                ('locus', models.PositiveSmallIntegerField(default=0)),
                ('page_type', models.CharField(choices=[('BPG', 'book pages'), ('GPG', 'game pages'), ('DPG', 'dashboard pages')], max_length=3)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('asset_type', models.CharField(choices=[('AUD', 'audio'), ('VID', 'video'), ('IMG', 'image'), ('TXT', 'text')], max_length=3)),
                ('content_text', models.TextField(max_length=5000)),
                ('file', models.FileField(default='default_cover.jpg', upload_to=book.models.media_upload_handler)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('cover', models.ImageField(default='default_cover.jpg', upload_to=book.models.cover_media_upload_handler)),
                ('author', models.CharField(max_length=256)),
                ('publisher', models.CharField(max_length=256)),
                ('pub_date', models.CharField(blank=True, max_length=64, null=True)),
                ('copyright', models.CharField(blank=True, max_length=64, null=True)),
                ('isbn', models.CharField(blank=True, max_length=17, null=True)),
                ('reading_level', models.CharField(blank=True, max_length=32, null=True)),
                ('word_count', models.CharField(blank=True, max_length=5, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('webpage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='pages.Page')),
            ],
        ),
        migrations.CreateModel(
            name='BookPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('name', models.CharField(blank=True, max_length=245, null=True)),
                ('is_title_page', models.BooleanField(default=False)),
                ('page_order', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('headline', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='book.Book')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='bookpage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visuals', to='book.BookPage'),
        ),
    ]
