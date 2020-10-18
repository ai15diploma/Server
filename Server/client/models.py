from django.db import models
from django.contrib.auth import get_user_model
from route.models import Stop

User = get_user_model()


class ActivePassengers(models.Model):
    idPassengers = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    idStop = models.CharField(max_length=4, blank=False)
    ToStop = models.ForeignKey(Stop, on_delete=models.CASCADE,blank=False)
    idDriver = models.CharField(max_length=4, blank=False, default= '0')