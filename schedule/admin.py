from django.contrib import admin

from schedule.models import *

admin.site.register(Semester)
admin.site.register(SchoolYear)
admin.site.register(Subject)
admin.site.register(ClassDay)
admin.site.register(ClassUnit)
admin.site.register(WeeklyTimetableEntry)
admin.site.register(TimetableEntry)
admin.site.register(NonLectiveDay)
admin.site.register(NonLectiveHours)
admin.site.register(ClassTrip)
