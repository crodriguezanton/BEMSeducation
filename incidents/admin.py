from django.contrib import admin
from .models import *

admin.site.register(Incident)
admin.site.register(IncidentType)
admin.site.register(IncidentCategory)
admin.site.register(Punishment)
admin.site.register(PunishmentType)