from django.shortcuts import render
from rest_framework import generics
from route.serializers import StopListSerializer, RouteListSerializer
from route.models import Stop, Route
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class StopListView(generics.ListAPIView):# список остановк
    serializer_class = StopListSerializer
    queryset = Stop.objects.all()
    permission_classes = (IsAuthenticated,)  # Если пользователь авторизован


class RouteListView(generics.ListAPIView):# список маршрутов
    serializer_class = RouteListSerializer
    queryset = Route.objects.all()
    permission_classes = (IsAuthenticated,)


class RouteDetailView(generics.RetrieveAPIView):# вывод маршрутов по id
    serializer_class = RouteListSerializer
    queryset = Route.objects.all()
    permission_classes = (IsAuthenticated,)

class StopDetailView(generics.RetrieveAPIView):# вывод остановок по id
    serializer_class = StopListSerializer
    queryset = Stop.objects.all()
    permission_classes = (IsAuthenticated,)



class EditStop(generics.RetrieveUpdateDestroyAPIView):#редактирование остановок
    serializer_class = StopListSerializer
    queryset = Stop.objects.all()
    permission_classes = (IsAdminUser,)


class EditRoute(generics.RetrieveUpdateDestroyAPIView):#редактирование маршрутов
    serializer_class = RouteListSerializer
    queryset = Route.objects.all()
    permission_classes = (IsAdminUser,)
