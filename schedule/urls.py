from django.conf.urls import url

from schedule.views import TimetableView

urlpatterns = [
    url(r'^timetable/(?P<year>[0-9]{4})/(?P<week>[0-9]+)/$', TimetableView.as_view(), name='timetable'),
]