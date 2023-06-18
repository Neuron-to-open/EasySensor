from django.db import models

# Create your models here.
class Soil(models.Model):
    airhum = models.CharField(max_length=10)
    sun = models.CharField(max_length=10)
    soilhum = models.CharField(max_length=10)
    temp = models.CharField(max_length=10)
