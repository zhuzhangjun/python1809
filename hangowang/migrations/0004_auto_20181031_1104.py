# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-31 11:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangowang', '0003_auto_20181029_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lunbotu',
            old_name='imgsrc',
            new_name='src',
        ),
    ]