# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtrip',
            name='students',
            field=models.ManyToManyField(blank=True, to='education.Student'),
        ),
        migrations.AlterField(
            model_name='nonlectiveperiod',
            name='grades',
            field=models.ManyToManyField(blank=True, to='institution.Grade'),
        ),
        migrations.AlterField(
            model_name='nonlectiveperiod',
            name='groups',
            field=models.ManyToManyField(blank=True, to='institution.Group'),
        ),
        migrations.AlterField(
            model_name='nonlectiveperiod',
            name='stages',
            field=models.ManyToManyField(blank=True, to='institution.Stage'),
        ),
    ]
