# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Schedule, Appointment

# Register your models here.

admin.site.register(Schedule)
admin.site.register(Appointment)