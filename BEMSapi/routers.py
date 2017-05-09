from rest_framework import routers
from BEMSapi.viewsets import TimetableEntryViewSet

default_router = routers.DefaultRouter()
default_router.register(r'timetable_entry', TimetableEntryViewSet, base_name='timetable_entry-detail')