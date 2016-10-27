# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_parent_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='responsible',
            field=models.ManyToManyField(blank=True, null=True, to='education.Parent'),
        ),
    ]