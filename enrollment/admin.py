from django.contrib import admin

from enrollment.models import *

admin.site.register(YearEnroll)
admin.site.register(ClassEnroll)
admin.site.register(MajorEnroll)