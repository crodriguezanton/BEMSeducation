from __future__ import print_function
from datetime import timedelta

from schedule.constants import DAY_CHOICES
from schedule.models import Semester, WeeklyTimetableEntry, ClassDay, TimetableEntry


def generate_timetable_entries(semester):

    delta = semester.end - semester.start
    wtes=WeeklyTimetableEntry.objects.all()
    for i in range(delta.days + 1):
        day = semester.start + timedelta(days=i)
        fwtes = wtes.filter(day=ClassDay.objects.filter(day=day.isoweekday()).first())
        for fwte in fwtes:
            TimetableEntry.objects.get_or_create(
                weekly_timetable_entry=fwte,
                date=day,
                active=fwte.class_active(day)
            )