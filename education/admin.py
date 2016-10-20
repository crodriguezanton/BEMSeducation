from django.contrib import admin

from education.models import *

admin.site.register(BEMSeducationInstance)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Teacher)