from django.db import models


# Create your models here.
class Cars(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    car = models.CharField(max_length=100)
    cmp = models.CharField(max_length=100)
