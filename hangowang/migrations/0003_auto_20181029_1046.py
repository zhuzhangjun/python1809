# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-29 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangowang', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='addr',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]