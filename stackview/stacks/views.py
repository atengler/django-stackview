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

from stackview.mixins import LoginRequired

from .forms import StackCreateForm
from .models import Stack
from .tables import StackTable

LOG = logging.getLogger(__name__)
User = get_user_model()


class CreateStackView(LoginRequired, FormView):
    template_name = 'stacks/create.html'
    form_class = StackCreateForm
    success_url = reverse_lazy('stacks:overview')

    def form_valid(self, form):
        form.save_stack(self.request.user)
        return super(CreateStackView, self).form_valid(form)


class OverviewView(LoginRequired, TemplateView):
    template_name = 'stacks/overview.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(OverviewView, self).get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated():
            stacks = Stack.objects.filter(tenant=self.request.user.tenantmembership.tenant)
            table = StackTable(stacks)
            RequestConfig(self.request).configure(table)
            ctx['stacks'] = table
        else:
            ctx['stacks'] = {}

        return ctx

