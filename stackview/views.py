# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

LOG = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = 'index.html'

