from __future__ import print_function
from datetime import timedelta

from schedule.constants import DAY_CHOICES
from schedule.models import Semester, WeeklyTimetableEntry, ClassDay, TimetableEntry


def generate_timetable_entries(semester):

    delta = semester.start - semester.end
    wtes=WeeklyTimetableEntry.objects.all()
    print(wtes)
    print(delta)
    for i in range(delta.days + 1):
        print(str(i))
        day = semester.start + timedelta(days=i)
        fwtes = wtes.filter(day=ClassDay.objects.get(day=day.isoweekday()))
        print(fwtes.all())
        for fwte in fwtes:
            print('loop')
            TimetableEntry.objects.get_or_create(
                weekly_timetable_entry=fwte,
                day=day,
                active=fwte.class_active(day)
            )