"""BEMSeducation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext

from BEMSeducation import settings
from education.views import MaintenanceView

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('BEMSauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', MaintenanceView.as_view(), name='index'),
    url(r'^attendance/', include('attendance.urls', namespace='attendance')),
    url(r'^enrollment/', include('enrollment.urls', namespace='enrollment')),
    url(r'^institution/', include('institution.urls', namespace='institution')),
    url(r'schedule/', include('schedule.urls', namespace='schedule')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

def handler404(request):
    response = render_to_response('special/404.html')
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('special/500.html')
    response.status_code = 500
    return response