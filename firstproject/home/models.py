from django.db import models


# Create your models here.
class Student(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    place = models.CharField(max_length=100)
