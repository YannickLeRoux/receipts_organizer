# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-11 04:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receipts', '0003_auto_20171210_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.CharField(db_index=True, max_length=13, primary_key=True, serialize=False, unique=True)),
                ('scan', models.FileField(blank=True, null=True, upload_to='receipts/%Y/%m/%d')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='receipts.Category')),
                ('recorded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='document',
            name='category',
        ),
        migrations.RemoveField(
            model_name='document',
            name='recorded_by',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
