from django.shortcuts import render
from django.views.generic import ListView
from .models import Student

# Create your views here.

class IndexView(ListView):
    model = Student
