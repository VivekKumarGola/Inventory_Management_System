from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import *

# Create your models here.
class Inventory(models.Model):
    product_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

def __str__(self):
    return self.product_name
