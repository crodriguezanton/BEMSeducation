from rest_framework import permissions
from rest_framework import viewsets

from BEMSapi.serializers import TimetableEntrySerializer
from schedule.models import TimetableEntry


class TimetableEntryViewSet(viewsets.ModelViewSet):
    queryset = TimetableEntry.objects.all()
    serializer_class = TimetableEntrySerializer
