# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.CharField(choices=[(b'F', b'Falta'), (b'R', b'Retard'), (b'J', b'Justified'), (b'C', b'Consergeria')], default='F', max_length=3)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Student')),
            ],
            options={
                'verbose_name': "Registre d'Assist\xe8ncia",
                'verbose_name_plural': "Registres d'Assist\xe8ncia",
            },
        ),
    ]
