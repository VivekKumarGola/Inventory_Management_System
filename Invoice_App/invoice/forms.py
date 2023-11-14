from django.core import validators
from django import forms
from .models import Invoice 
from django.forms import ModelForm
from .models import User

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name','customer_gst','phone','product_name','quantity','price','total','netamount','date']