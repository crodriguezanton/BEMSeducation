from django.conf.urls import url

from incidents.views import IncidentCreateView, IncidentListView, ReviewIncidentListView

urlpatterns = [
    url(r'^create$', IncidentCreateView.as_view(), name='create'),
    url(r'^list/$', IncidentListView.as_view(), name='list'),
    url(r'^review$', ReviewIncidentListView.as_view(), name='review'),
]