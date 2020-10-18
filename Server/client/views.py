from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import ClientSerializers
from .models import ActivePassengers


class ClientCreateView(generics.CreateAPIView):
    serializer_class = ClientSerializers
    queryset = ActivePassengers.objects.all()
    permission_classes = (IsAuthenticated,)


class ClientListView(generics.ListAPIView):
    serializer_class = ClientSerializers
    queryset = ActivePassengers.objects.all()
    permission_classes = (IsAuthenticated,)


class ClientEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializers
    queryset = ActivePassengers.objects.all()
    permission_classes = (IsAuthenticated,)
