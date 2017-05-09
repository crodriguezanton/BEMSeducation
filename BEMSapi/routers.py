from rest_framework import routers
from BEMSapi.viewsets import TimetableEntryViewSet, TimetableDayViewSet, CallViewSet

default_router = routers.DefaultRouter()
default_router.register(r'timetable_entry', TimetableEntryViewSet, base_name='timetable_entry-detail')
default_router.register(r'timetable_entry_day', TimetableDayViewSet, base_name='timetable_entry-day')
default_router.register(r'timetable_entry_call', CallViewSet, base_name='timetable_entry-call')