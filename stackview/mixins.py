from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy


class LoginRequired(LoginRequiredMixin):
    login_url = reverse_lazy('identity:login')
    redirect_field_name = 'next'

