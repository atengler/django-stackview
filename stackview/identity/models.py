# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Tenant(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Stack Name'))
    created = models.DateTimeField(auto_now_add=True, blank=True)


class TenantMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    user = models.OneToOneField(Tenant, on_delete=models.CASCADE, verbose_name=_('Tenant'))
    created = models.DateTimeField(auto_now_add=True, blank=True)

