# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_number',
            field=models.IntegerField(default=293348),
            preserve_default=False,
        ),
    ]
