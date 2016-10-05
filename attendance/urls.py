from django.conf.urls import url

from attendance.views import AttendanceEntryListView, RankingListView

urlpatterns = [
    url(r'^entry/$', AttendanceEntryListView.as_view()),
    url(r'^ranking/$', RankingListView.as_view()),
]