# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Stack(models.Model):
    BACKEND_CHOICES = (
        ('aws', _('AWS')),
        ('os', _('OpenStack'))
    )

    STATUS_CHOICES = (
        ('success', _('Success')),
        ('fail', _('Fail')),
        ('unknown', _('Unknown'))
    )

    name = models.CharField(max_length=255, verbose_name=_('Stack Name'))
    backend = models.CharField(max_length=1, choices=BACKEND_CHOICES, verbose_name=_('Backend'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stacks', verbose_name=_('Author'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name=_('Status')) 
    created = models.DateTimeField(auto_now_add=True, blank=True)

