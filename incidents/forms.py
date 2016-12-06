from django.forms import ModelForm, CharField

from education.models import Student
from incidents.models import Incident, IncidentType


class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = ['teacher', 'type', 'category', 'date', 'unit', 'description', 'comments', 'accepted', 'returned', 'completed']

    students = CharField()

    def __init__(self, *args, **kwargs):
        super(IncidentForm, self).__init__(*args, **kwargs)
        self.fields['type'].required = False

    def clean_type(self):
        if self.cleaned_data.get('type', None) is None:
            return IncidentType.objects.first()
        else:
            return self.cleaned_data.get('type', None)

    def save(self, commit=True):

        if self.errors:
            raise ValueError(
                "The %s could not be %s because the data didn't validate." % (
                    self.instance._meta.object_name,
                    'created' if self.instance._state.adding else 'changed',
                )
            )

        instance = self.instance
        student_list = []
        students = self.cleaned_data.get('students', [])

        for student_pk in self.cleaned_data.get('students', "").split(","):
            instance.pk = None
            instance.student = Student.objects.get(pk=student_pk)
            instance.save()
            student_list.append(instance.pk)

        return Incident.objects.filter(pk__in=student_list)


class EditIncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = ['description', 'comments', 'accepted', 'returned', 'completed']
