# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20160302_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]
