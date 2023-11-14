from django.contrib import admin
from inventory.models import *
from .models import Inventory
# Register your models here.

class InventoryAdmin(admin.ModelAdmin):
    list_display=('product_name','company','quantity','price')

admin.site.register(Inventory, InventoryAdmin)
