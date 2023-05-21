from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    text = models.TextField(max_length=300)
    number = models.IntegerField()
    positive_num = models.PositiveIntegerField()


# author name, age, active_date, penname, journal

class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    active_date = models.DateField()
    penname = models.CharField(max_length=20)
    journal = models.TextField(max_length=100)

    