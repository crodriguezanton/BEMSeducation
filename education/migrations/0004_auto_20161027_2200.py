# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_auto_20161027_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='responsible',
            field=models.ManyToManyField(blank=True, to='education.Parent'),
        ),
    ]
