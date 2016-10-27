from debug_toolbar.middleware import DebugToolbarMiddleware
from django.http import HttpResponseRedirect
from django.urls import set_urlconf
from django.utils.deprecation import MiddlewareMixin

from BEMSconsole import settings


class ProfileMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        request.profile = request.user.bemsuser.bemsprofile_set.first()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

