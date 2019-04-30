# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Schedule(models.Model):
    title = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.title


class Appointment(models.Model):
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    start_time = models.IntegerField(null=False)
    end_time = models.IntegerField(null=False)

    def __str__(self):
        return self.title
    
    ## Prevents saving a smaller or equal to end time
    # def save(self, *args, **kwargs):
    #     if self.end_time <= self.start_time:
    #         return
    #     else:
    #         super(Appointment, self).save(*args, **kwargs)
