from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import StatisticListSerializer, ScheduleListSerializer
from .models import Statistic, Schedule

class StatisticEditView(generics.RetrieveDestroyAPIView):
    serializer_class = StatisticListSerializer
    queryset = Statistic.objects.all()
    #permission_classes = (IsAdminUser,)

class StatisticCreateView(generics.CreateAPIView):
    serializer_class = StatisticListSerializer
    queryset = Statistic.objects.all()
    #permission_classes = (IsAdminUser,)


class ScheduleAddView(generics.CreateAPIView):
    serializer_class = ScheduleListSerializer
    queryset = Schedule.objects.all()
    #permission_classes = (IsAdminUser,)


class ScheduleEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleListSerializer
    queryset = Schedule.objects.all()
    #permission_classes = (IsAdminUser,)




