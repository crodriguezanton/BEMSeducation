from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from BEMSapi.serializers import TimetableEntrySerializer
from schedule.models import TimetableEntry

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class TimetableEntryViewSet(viewsets.ModelViewSet):
    queryset = TimetableEntry.objects.all()
    serializer_class = TimetableEntrySerializer
    pagination_class = StandardResultsSetPagination
