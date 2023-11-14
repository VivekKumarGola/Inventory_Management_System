from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import *


# Create your models here.
class Invoice(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_gst = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    product_name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length=50)
    netamount = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    def __str__(self):
        return self.customer_name


class Product(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='invoice', on_delete=models.SET_NULL,null=True)
    product_name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length=50)
    netamount = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.product_name    
    
