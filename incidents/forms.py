from django.forms import ModelForm, CharField

from incidents.models import Incident


class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = ['teacher', 'type', 'category', 'date', 'timetable_entry', 'description', 'accepted', 'returned', 'completed']

    students = CharField()
