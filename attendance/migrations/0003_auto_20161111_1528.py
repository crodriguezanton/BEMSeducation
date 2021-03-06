# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20161027_0923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendanceentry',
            options={'verbose_name': 'Attendance Entry', 'verbose_name_plural': 'Attendance Entries'},
        ),
        migrations.AlterField(
            model_name='attendanceentry',
            name='type',
            field=models.CharField(choices=[(b'F', b'Absent'), (b'R', b'Delay'), (b'J', b'Justified'), (b'C', b'Consergeria')], default='F', max_length=3),
        ),
    ]
