from django.db import models
from django.contrib.auth import get_user_model
from route.models import Route, Stop
from django.contrib.postgres.fields import JSONField
from client.models import ActivePassengers

User = get_user_model()


class ActiveDriver(models.Model):
    idDriver = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    numberRoute = models.ForeignKey(Route, on_delete=models.CASCADE, )
    numberPassengers = models.ManyToManyField(ActivePassengers)
    Active = models.BooleanField(default=True)
    GPS = JSONField
    Locate = models.ForeignKey(Stop, on_delete=models.CASCADE)
