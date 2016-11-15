from __future__ import unicode_literals

import uuid as uuid
from BEMSauth.models import BEMSProfile
from django.db import models
from model_utils.models import TimeStampedModel

from education.models import Student, Teacher
from schedule.models import TimetableEntry


class IncidentType(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name


class PunishmentType(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class IncidentCategory(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Punishment(models.Model):
    type = models.ForeignKey(PunishmentType)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.type.name + " - " + self.student.__unicode__()


class Incident(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)

    student = models.ForeignKey(Student)
    teacher = models.ForeignKey(Teacher)

    type = models.ForeignKey(IncidentType)
    category = models.ForeignKey(IncidentCategory, null=True, blank=True)
    punishment = models.OneToOneField(Punishment, blank=True, null=True)

    date = models.DateField()
    timetable_entry = models.ForeignKey(TimetableEntry, null=True, blank=True)
    description = models.TextField()
    comments = models.TextField(blank=True, null=True)

    accepted = models.BooleanField(default=False)
    returned = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    created_by = models.ForeignKey(BEMSProfile, null=True, blank=True, related_name='incident_created_by')

    def __unicode__(self):
        return self.pk + ": " + self.student.__unicode__() + " - " + self.type.name
