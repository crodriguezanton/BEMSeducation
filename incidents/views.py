# coding=utf-8
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import ListView

from education.models import Student
from incidents.forms import IncidentForm
from incidents.models import Incident


class IncidentCreateView(CreateView):
    model = Incident
    form_class = IncidentForm

    def get_context_data(self, **kwargs):
        context = super(IncidentCreateView, self).get_context_data(**kwargs)

        context['title'] = 'Nova Incidència'

        #context['incidentTypes'] = IncidentType.objects.all()
        #context['students'] = Student.objects.all().order_by('surname', 'name')
        #context['teachers'] = Teacher.objects.all().order_by('surname', 'name').exclude(name='')
        #context['units'] = ClassUnit.objects.all().order_by('start')
        #context['categories'] = IncidentCategory.objects.all()
        #context['punishmentTypes'] = PunishmentType.objects.all()
        context['students'] = Student.objects.all()

        if self.request.GET.has_key('students'):
            context['getstu'] = self.request.GET.getlist('students')

        return context


class IncidentListView(ListView):
    model = Incident

    def get_context_data(self, **kwargs):
        context = super(IncidentListView, self).get_context_data(**kwargs)

        context['title'] = 'Incidents'

        context['activeincidents'] = Incident.objects.filter(teacher__teacherprofile__bemsuser__user=self.request.user, completed=False)
        context['pendingincidents'] = Incident.objects.filter(teacher__teacherprofile__bemsuser__user=self.request.user, accepted=False)
        context['archivedincidents'] = Incident.objects.filter(teacher__teacherprofile__bemsuser__user=self.request.user, completed=True)

        return context


class ReviewIncidentListView(IncidentListView):
    model = Incident

    def get_context_data(self, **kwargs):
        context = super(ReviewIncidentListView, self).get_context_data(**kwargs)

        if 'q' in self.request.GET:
            if self.request.GET['q'] != '*':
                context['newincidents'] = context['newincidents'].filter(student__pk=self.request.GET['q'])
                context['activeincidents'] = context['activeincidents'].filter(student__pk=self.request.GET['q'])
                context['archivedincidents'] = context['archivedincidents'].filter(student__pk=self.request.GET['q'])

        return context

