from BEMSauth.models import BEMSUser, UserRequest
from allauth.account.adapter import DefaultAccountAdapter
from django.core.exceptions import SuspiciousOperation


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super(AccountAdapter, self).save_user(request, user, form, commit=commit)
        request_id = form.cleaned_data.get('profile', "")

        if not hasattr(user, 'bemsuser'):
            BEMSUser.objects.create(user=user)

        if not request_id == "":
            user_request = UserRequest.objects.get(pk=request_id)
            if user_request.used:
                raise SuspiciousOperation()

            profile = user_request.profile
            profile.bemsuser = user.bemsuser
            user_request.used = True

            profile.save()
            user_request.save()
        else:
            raise SuspiciousOperation()
        return user

    def get_login_redirect_url(self, request):
        return 'http://edu.bems.cat'
