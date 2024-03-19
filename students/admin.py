from django.contrib import admin
from .models import Students, StudentParents

# Register your models here.
admin.site.register([Students, StudentParents])