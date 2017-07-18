# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.contrib.auth import authenticate, login, get_user_model
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, FormView

from .forms import LoginForm, UserUpdateForm

LOG = logging.getLogger(__name__)
User = get_user_model()


class UserUpdateView(UpdateView):
    model = User
    template_name = "identity/user_update_form.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        ctx = super(UserUpdateView, self).get_context_data(*args, **kwargs)
        ctx['user_id'] = None
        pk = self.kwargs.get('pk', None)
        if pk:
            ctx['user_id'] = int(pk)

        return ctx


class LoginView(FormView):
    template_name = 'identity/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = None
        username = form.cleaned_data.get('username', None)
        password = form.cleaned_data.get('password', None)

        if username and password:
            user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)

        return super(LoginView, self).form_valid(form)

