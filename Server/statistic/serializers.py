from rest_framework import serializers
from .models import Statistic, Schedule


class StatisticListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'

class ScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'