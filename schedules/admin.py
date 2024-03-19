from django.contrib import admin
from .models import Schedules, TeacherPresenceSchedules

# Register your models here.

admin.site.register([Schedules, TeacherPresenceSchedules])