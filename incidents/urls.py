from django.conf.urls import url

from incidents.views import IncidentCreateView, IncidentListView, ReviewIncidentListView, MyIncidentListView, IncidentCardView

urlpatterns = [
    url(r'^create$', IncidentCreateView.as_view(), name='create'),
    url(r'^list/$', MyIncidentListView.as_view(), name='list'),
    url(r'^review$', ReviewIncidentListView.as_view(), name='review'),
    url(r'^card/(?P<pk>[^/]+)/$', IncidentCardView.as_view(), name='card')
]