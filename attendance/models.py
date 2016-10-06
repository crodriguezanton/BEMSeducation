from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel

from main.models import Student, BEMSeducationInstance
from schedule.models import TimetableEntry


class AttendanceType(models.Model):

    class Meta:
        verbose_name = _('Attendance Type')
        verbose_name_plural = _('Attendance Types')
        unique_together = ('instance', 'char')

    name = models.CharField(max_length=100)
    instance = models.ForeignKey(BEMSeducationInstance, blank=True, null=True)
    char = models.CharField(max_length=3)
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return self.char + ": " + self.name


class AttendanceEntry(TimeStampedModel):

    class Meta:
        verbose_name = _('Attendance Entry')
        verbose_name_plural = _('Attendance Entries')
        unique_together = ('student', 'timetable_entry')

    student = models.ForeignKey(Student)
    timetable_entry = models.ForeignKey(TimetableEntry, blank=True, null=True)
    type = models.ForeignKey(AttendanceType)

    def is_justified(self):
        if self.type == AttendanceType.objects.get(char='J'):
            return True
        return False
