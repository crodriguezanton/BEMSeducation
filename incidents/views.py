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

        context['activeincidents'] = Incident.objects.filter(teacher=self.request.profile, completed=False)
        context['pendingincidents'] = Incident.objects.filter(teacher=self.request.profile, accepted=False)
        context['archivedincidents'] = Incident.objects.filter(teacher=self.request.profile, completed=True)

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


class IncidentCardView(UpdateView):
    template_name_suffix = '_card'
    form_class = EditIncidentForm
    model= Incident
    success_url = '/incidents/list/'

    def get_success_url(self):
        return reverse('incidents:list') + "#" + str(self.object.pk)


def incident_status(request, pk=None, status=None, value='True'):

    if value == 'True':
        value = True
    else:
        value = False

    incident = Incident.objects.get(pk=pk)

    if status == 'accepted':
        incident.accepted = value
    elif status == 'returned':
        incident.returned = value
    elif status == 'completed':
        incident.completed = value

    incident.save()


    return HttpResponseRedirect(request.META['HTTP_REFERER'])