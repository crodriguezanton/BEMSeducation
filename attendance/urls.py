from django.conf.urls import url

from attendance.views import AttendanceEntryListView, RankingListView, TodayCallView, CallView

urlpatterns = [
    url(r'^entry/$', AttendanceEntryListView.as_view(), name='entry-list'),
    url(r'^ranking/$', RankingListView.as_view(), name='ranking'),
    url(r'^call/today$', TodayCallView.as_view(), name='call-today'),
    url(r'^call/(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$', CallView.as_view(), name='call'),
]