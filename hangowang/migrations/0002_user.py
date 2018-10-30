# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-29 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangowang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=256)),
                ('addr', models.CharField(max_length=256)),
                ('token', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]