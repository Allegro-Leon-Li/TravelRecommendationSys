# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20161130_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='users',
            name='account',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
