# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-27 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lunbotu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('imgsrc', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Lunbotu',
            },
        ),
    ]
