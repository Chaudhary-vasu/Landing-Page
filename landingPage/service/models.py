from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
# Create your models here.

class Service(models.Model):
    service_icon = models.CharField(max_length=20)
    service_title = models.CharField(max_length=50)
    service_des = models.TextField()
    # service_slug = AutoSlugField(populate_from = "service_icon",unique=True,null=True,default=None)

class Servicecard(models.Model):
    service_image = models.FileField(upload_to="service/",max_length=250,null=True,default=None)
    service_card_title = models.CharField(max_length=50)
    service_card_intro  = models.CharField(max_length=100)
