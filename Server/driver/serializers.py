from rest_framework import serializers
from .models import ActiveDriver
from client.models import ActivePassengers




class ActiveDriveSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActiveDriver
        fields = '__all__'




class ActiveDriveFilterSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivePassengers
        fields = '__all__'