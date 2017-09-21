# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0002_auto_20170921_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='freq',
            field=models.CharField(choices=[('a', 'annual'), ('q', 'quarterly'), ('m', 'monthly'), ('w', 'weekly'), ('d', 'daily')], max_length=1),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]