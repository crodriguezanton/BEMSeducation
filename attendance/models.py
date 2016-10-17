from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel

from attendance.constants import ATTENDANCE_TYPE_CHOICES
from main.models import Student, BEMSeducationInstance
from schedule.models import TimetableEntry


class AttendanceEntry(TimeStampedModel):

    class Meta:
        verbose_name = _('Attendance Entry')
        verbose_name_plural = _('Attendance Entries')
        unique_together = ('student', 'timetable_entry')

    student = models.ForeignKey(Student)
    timetable_entry = models.ForeignKey(TimetableEntry, blank=True, null=True)
    type = models.CharField(max_length=3, choices=ATTENDANCE_TYPE_CHOICES, default='F')

    def is_justified(self):
        return self.type is 'J'
