# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 15:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0003_auto_20161027_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subjectenroll',
            options={'verbose_name': 'Subject Enrollment', 'verbose_name_plural': 'Subject Enrollments'},
        ),
        migrations.AlterModelOptions(
            name='yearenroll',
            options={'verbose_name': 'Student Enrollment', 'verbose_name_plural': 'Student Enrollments'},
        ),
    ]
