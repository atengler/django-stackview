# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.contrib.auth import authenticate, login, get_user_model
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django_tables2 import RequestConfig

from .forms import StackCreateForm, LoginForm, UserUpdateForm
from .models import Stack
from .tables import StackTable

LOG = logging.getLogger(__name__)
User = get_user_model()


class CreateStackView(FormView):
    template_name = 'stacks/create.html'
    form_class = StackCreateForm
    success_url = reverse_lazy('stacks:home')

    def form_valid(self, form):
        form.save_stack(self.request.user)
        return super(CreateStackView, self).form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    template_name = "auth/user_update_form.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy('stacks:home')

    def get_context_data(self, *args, **kwargs):
        ctx = super(UserUpdateView, self).get_context_data(*args, **kwargs)
        ctx['user_id'] = None
        pk = self.kwargs.get('pk', None)
        if pk:
            ctx['user_id'] = int(pk)

        return ctx


class HomePageView(FormView):
    template_name = 'stacks/home.html'
    form_class = LoginForm
    success_url = reverse_lazy('stacks:home')

    def get_context_data(self, *args, **kwargs):
        ctx = super(HomePageView, self).get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated():
            stacks = Stack.objects.filter(author=self.request.user)
            table = StackTable(stacks)
            RequestConfig(self.request).configure(table)
            ctx['stacks'] = table
        else:
            ctx['stacks'] = {}

        return ctx

    def form_valid(self, form):
        user = None
        username = form.cleaned_data.get('username', None)
        password = form.cleaned_data.get('password', None)

        if username and password:
            user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)

        return super(HomePageView, self).form_valid(form)

