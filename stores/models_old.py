from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    descriptions = models.CharField(max_length=200, default='')
    # image = models.ImageField(upload_to='products/')
