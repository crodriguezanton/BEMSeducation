from django.contrib import admin

from attendance.models import AttendanceType, AttendanceEntry

admin.site.register(AttendanceType)
admin.site.register(AttendanceEntry)
