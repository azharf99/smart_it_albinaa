from django.contrib import admin
from .models import TeachersPresences, TeachersClassPresences

# Register your models here.
admin.site.register([TeachersPresences, TeachersClassPresences])