# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 23:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20161111_1528'),
        ('incidents', '0002_auto_20161115_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='timetable_entry',
        ),
        migrations.AddField(
            model_name='incident',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.ClassUnit'),
        ),
    ]
