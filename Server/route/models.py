from django.db import models
from django.contrib.postgres.fields import  JSONField




class Stop(models.Model):
    id = models.AutoField(primary_key=True)
    stopName = models.CharField(max_length=80)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    routeName = models.CharField(max_length=101)
    busNumber = models.IntegerField()
    Stops = JSONField()
