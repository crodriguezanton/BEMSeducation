from django_filters import FilterSet

from attendance.models import AttendanceEntry
from main.models import Student


class AttendanceEntryFilter(FilterSet):
    class Meta:
        model = AttendanceEntry
        fields = {
            'type__char':                                              ['exact'],
            'student__first_name':                                     ['exact', 'icontains'],
            'student__last_name':                                      ['exact', 'icontains'],
            'student__studentstatus__group__short_name':               ['exact'],
            'student__studentstatus__group__grade__short_name':        ['exact'],
            'student__studentstatus__group__grade__stage__short_name': ['exact'],
            'timetable_entry__date':                                   ['exact', 'gte', 'lte'],
        }


class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name':                                     ['exact', 'icontains'],
            'last_name':                                      ['exact', 'icontains'],
            'studentstatus__group__short_name':               ['exact'],
            'studentstatus__group__grade__short_name':        ['exact'],
            'studentstatus__group__grade__stage__short_name': ['exact'],
        }
