from django.contrib import admin

from schedule.models import *

admin.site.register(Semester)
admin.site.register(SchoolYear)
admin.site.register(Subject)
admin.site.register(MajorSubject)
admin.site.register(ClassDay)
admin.site.register(ClassUnit)
admin.site.register(WeeklyTimetableEntry)
admin.site.register(TimetableEntry)
