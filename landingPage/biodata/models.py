from django.db import models
# Create your models here.

class Biodata(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    rollno = models.CharField(max_length=10)
    email = models.EmailField(blank=True,verbose_name="Email Address")
    phonenumber = models.IntegerField(max_length=10)