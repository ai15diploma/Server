from rest_framework import serializers
from .models import ActivePassengers


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivePassengers
        fields = '__all__'