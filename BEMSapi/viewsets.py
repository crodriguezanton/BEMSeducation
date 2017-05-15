import datetime

from django.shortcuts import get_object_or_404
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from BEMSapi.serializers import TimetableEntrySerializer, StudentStatusSerializer
from education.models import Student
from schedule.models import TimetableEntry

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class TimetableEntryViewSet(viewsets.ModelViewSet):
    serializer_class = TimetableEntrySerializer
    pagination_class = StandardResultsSetPagination
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        te = TimetableEntry.objects.filter(weekly_timetable_entry__teacher__pk="d1864d7e-b772-4aae-bb30-cd02a1a275c8")
        te = te.filter(date__gte=datetime.datetime.fromtimestamp(int(self.request.GET.get('start', ''))), date__lte=datetime.datetime.fromtimestamp(int(self.request.GET.get('end', ''))))
        return te


class TimetableDayViewSet(viewsets.ModelViewSet):
    serializer_class = TimetableEntrySerializer
    pagination_class = StandardResultsSetPagination
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        te = TimetableEntry.objects.filter(weekly_timetable_entry__teacher__pk="d1864d7e-b772-4aae-bb30-cd02a1a275c8").order_by('weekly_timetable_entry__unit__start')
        te = te.filter(date=self.request.GET.get('day', ''))
        return te


class CallViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudentStatusSerializer
    pagination_class = StandardResultsSetPagination
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        timetable_entry = get_object_or_404(TimetableEntry, pk=self.request.GET.get('timetable_entry', 0))
        students = Student.objects.filter(yearenroll__group=timetable_entry.weekly_timetable_entry.group).order_by('last_name', 'first_name')
        for stu in students:
            stu.status = stu.attendanceentry_set.filter(timetable_entry=timetable_entry).first()

        return students
