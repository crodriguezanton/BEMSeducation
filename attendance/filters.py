from django_filters import FilterSet

from attendance.models import AttendanceEntry

from django_filters import filters

filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than'),
    ('gt', 'Greater than'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('not_contains', 'Does not contain'),
]


class AttendanceEntryFilter(FilterSet):
    class Meta:
        model = AttendanceEntry
        fields = ['student', 'type', 'student__first_name', 'student__last_name',]