
class ProfileMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.user.is_authenticated():
            if hasattr(request.user, 'bemsuser'):
                request.profile = request.user.bemsuser.bemsprofile_set.first()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
