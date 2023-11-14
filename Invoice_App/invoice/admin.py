from django.contrib import admin
from invoice.models import *
from .models import Invoice, Product
# Register your models here.


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display=('customer_name','customer_gst','phone','product_name','quantity','price','total','netamount','date')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass