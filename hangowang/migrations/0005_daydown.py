# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-31 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangowang', '0004_auto_20181031_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daydown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgsrc', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'daydown',
            },
        ),
    ]
