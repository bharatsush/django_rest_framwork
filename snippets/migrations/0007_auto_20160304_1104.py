# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20160304_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
