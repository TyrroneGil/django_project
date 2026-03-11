from django.db import models

# Create your models here.
class Profile(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)

class Students(models.Model):
    fullname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.IntegerField()

class School(models.Model):
    school_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=5)
        