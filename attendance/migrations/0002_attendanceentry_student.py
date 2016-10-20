# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-18 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0001_initial'),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendanceentry',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Student'),
        ),
    ]
