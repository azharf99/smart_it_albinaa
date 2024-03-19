from django.contrib import admin
from .models import Assessments, AssessmentsAnswerSheets, AssessmentSchedules, AssessmentsTypes

# Register your models here.

admin.site.register([Assessments, AssessmentsAnswerSheets, AssessmentSchedules, AssessmentsTypes])