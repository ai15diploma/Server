from rest_framework import serializers
from route.models import Stop, Route


class StopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = '__all__'


class RouteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'
