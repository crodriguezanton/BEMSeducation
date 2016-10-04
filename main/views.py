from django.shortcuts import render
from django.views.generic import TemplateView


class MaintenanceView(TemplateView):
    template_name = 'special/maintenance.html'
