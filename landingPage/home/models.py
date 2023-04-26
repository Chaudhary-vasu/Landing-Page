from django.db import models

# Create your models here.
class Home(models.Model):
    home_logo = models.CharField(max_length=10)

class HomeForm(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    