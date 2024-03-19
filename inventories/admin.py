from django.contrib import admin
from .models import Inventories, InventoryStatus

# Register your models here.

admin.site.register([Inventories, InventoryStatus])