# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 12:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfield',
            name='date_of_addition',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 16, 12, 29, 41, 162566)),
        ),
    ]
