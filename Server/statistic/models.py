from django.db import models
from django.contrib.postgres.fields import ArrayField
from route.models import Route

class Statistic(models.Model):
    Date = models.TextField()
    Statist = models.TextField()

class Schedule(models.Model):
    routeId = models.ForeignKey(Route, on_delete=models.DO_NOTHING)
    dayOff = models.BooleanField(blank=True)
    departure = ArrayField(models.CharField(max_length=5), blank=True)
    arrival = ArrayField(models.CharField(max_length=5), blank=True)