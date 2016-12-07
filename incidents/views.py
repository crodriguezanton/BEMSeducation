# coding=utf-8
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django_filters.views import FilterView

from education.models import Student
from incidents.filters import IncidentFilter
from incidents.forms import IncidentForm, EditIncidentForm
from incidents.models import Incident


class IncidentCreateView(CreateView):
    model = Incident
    form_class = IncidentForm
    success_url = '/'

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


class IncidentListView(FilterView):
    model = Incident
    filterset_class = IncidentFilter
    template_name_suffix = '_list'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(IncidentListView, self).get_context_data(**kwargs)

        context['title'] = 'Incidents'
        context['page_aside'] = True

        return context

class ReviewIncidentListView(IncidentListView):
    pass


class MyIncidentListView(IncidentListView):

    def get_queryset(self):
        queryset = super(IncidentListView, self).get_queryset()

        return queryset.filter(teacher=self.request.profile)


class IncidentCardView(UpdateView):
    template_name_suffix = '_card'
    form_class = EditIncidentForm
    model= Incident
    success_url = '/incidents/list/'

    def get_success_url(self):
        return reverse('incidents:review') + "#" + str(self.object.pk)
