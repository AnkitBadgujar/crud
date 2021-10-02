from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=155,blank=False)
    roll_no = models.IntegerField()
    Class = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    
    