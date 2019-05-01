# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets, generics, status
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
        schedule = Schedule.objects.get(id=self.kwargs['pk'])
        schedule.delete()
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

        largest_start_time = Appointment.objects.filter(
                                schedule=request.POST['schedule']
                                ).values('start_time').order_by('-start_time')[0]

        max_starttime = largest_start_time['start_time']

        largest_end_time = Appointment.objects.filter(
                                schedule=request.POST['schedule']
                                ).values('end_time').order_by('-end_time')[0]

        max_endtime = largest_end_time['end_time']

        if request.POST['start_time'] >= request.POST['end_time']:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        elif request.POST['start_time'] >= max_starttime:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        elif request.POST['start_time'] <= max_endtime:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(serializer.data)

    def perform_create(self, serializer):
            serializer.save()

    def destroy(self, request, pk=None):      
        schedule = Appointment.objects.get(id=self.kwargs['pk'])
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)