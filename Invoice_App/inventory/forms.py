from django.core import validators
from django import forms
from .models import Inventory 
from django.forms import ModelForm
from .models import User

class InventoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product_name','company','quantity','price']