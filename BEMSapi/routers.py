from rest_framework import routers
from BEMSapi.viewsets import TimetableEntryViewSet, CallViewSet

default_router = routers.DefaultRouter()
default_router.register(r'timetable_entry', TimetableEntryViewSet, base_name='timetable_entry-detail')
default_router.register(r'timetable_entry_call', CallViewSet, base_name='timetable_entry-call')