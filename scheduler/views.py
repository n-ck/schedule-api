# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Schedule, Appointment
from .serializers import ScheduleSerializer, AppointmentSerializer



class ScheduleView(viewsets.ModelViewSet):

    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Appointment.objects.filter(schedule=self.kwargs['pk'])

    def retrieve(self, request, pk=None):
        sched = self.kwargs['pk']
        queryset = Appointment.objects.filter(schedule=sched).order_by('start_time')
        serializer = ScheduleSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, pk=None):
        # sched = self.kwargs['pk']        
        schedule = Schedule.objects.get(id=self.kwargs['pk'])
        schedule.delete()
        #perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentView(viewsets.ModelViewSet):

    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.get(id=self.kwargs['pk'])

    def retrieve(self, request, pk=None):
        queryset = Appointment.objects.filter(pk=self.kwargs['pk'])
        serializer = ScheduleSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, pk=None):
        # sched = self.kwargs['pk']        
        schedule = Appointment.objects.get(id=self.kwargs['pk'])
        schedule.delete()
        #perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)