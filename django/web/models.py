from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    activated = models.BooleanField()

class Event(models.Model):
    name = models.CharField(max_length=100)
