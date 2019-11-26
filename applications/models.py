from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    key = models.IntegerField(null=True)
    owner = models.ForeignKey('auth.User', related_name='application', null=True, on_delete=models.CASCADE)