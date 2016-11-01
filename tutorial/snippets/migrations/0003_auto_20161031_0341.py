# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ('created',)},
        ),
        migrations.AlterField(
            model_name='users',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'english'), ('de', 'german'), ('it', 'italian'), ('ot', 'others')], default='en', max_length=100),
        ),
    ]