from django_filters import FilterSet

from incidents.models import Incident


class IncidentFilter(FilterSet):
    class Meta:
        model = Incident
        fields = {
            'accepted': ['exact'],
            'returned': ['exact'],
            'completed': ['exact'],
        }
