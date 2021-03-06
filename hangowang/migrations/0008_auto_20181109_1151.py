# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-09 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hangowang', '0007_goodlists'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaydownDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(default=None, max_length=50)),
                ('imgsrc', models.CharField(max_length=50)),
                ('middleimg1', models.CharField(default=None, max_length=50)),
                ('middleimg2', models.CharField(default=None, max_length=50)),
                ('middleimg3', models.CharField(default=None, max_length=50)),
                ('middleimg4', models.CharField(default=None, max_length=50)),
                ('smallimg1', models.CharField(default=None, max_length=50)),
                ('smallimg2', models.CharField(default=None, max_length=50)),
                ('smallimg3', models.CharField(default=None, max_length=50)),
                ('smallimg4', models.CharField(default=None, max_length=50)),
                ('bigimg1', models.CharField(default=None, max_length=50)),
                ('bigimg2', models.CharField(default=None, max_length=50)),
                ('bigimg3', models.CharField(default=None, max_length=50)),
                ('bigimg4', models.CharField(default=None, max_length=50)),
                ('dtbgimg1', models.CharField(default=None, max_length=50)),
                ('dtbgimg2', models.CharField(default=None, max_length=50)),
                ('dtbgimg3', models.CharField(default=None, max_length=50)),
                ('dtbgimg4', models.CharField(default=None, max_length=50)),
                ('dtbgimg5', models.CharField(default=None, max_length=50)),
                ('dtbgimg6', models.CharField(default=None, max_length=50)),
                ('dtbgimg7', models.CharField(default=None, max_length=50)),
                ('dtbgimg8', models.CharField(default=None, max_length=50)),
                ('hint', models.CharField(default=None, max_length=50)),
                ('evaluate', models.CharField(default=None, max_length=10)),
                ('repertory', models.CharField(default=None, max_length=10)),
                ('title', models.CharField(default=None, max_length=100)),
                ('unit', models.CharField(default=None, max_length=10)),
                ('price', models.CharField(default=None, max_length=10)),
                ('original', models.CharField(default=None, max_length=10)),
            ],
            options={
                'db_table': 'daydown_Detail',
            },
        ),
        migrations.AlterField(
            model_name='daydown',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='daydowndetail',
            name='daydown',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hangowang.Daydown'),
        ),
    ]
