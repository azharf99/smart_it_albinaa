from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from django.core import serializers
from .models import Scores
from .foms import ScoreCreateForm
from subjects.models import Subjects
from teachers.models import Teachers
import json

# Create your views here.

class ScoresIndex(ListView):
    model = Scores


def createScore(request):
    classes = Subjects.objects.select_related("subject_class", "subject_teacher", "subject_schedule").filter(subject_teacher=request.user.teachers)
    data = serializers.serialize("json", Teachers.objects.all())
    data_json = json.loads(data)
    context={
        'classes': classes,
        'data': data_json,
    }
    return render(request, 'scores/scores_form.html',  context)
    return JsonResponse(*data_json)