from typing import Any
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, FormView
from django.core import serializers
from django.db.models import F
from .models import Scores
from .foms import ScoreCreateForm
from subjects.models import Subjects
from students.models import Students
from teachers.models import Teachers
from grades.models import Classes
from schedules.models import Schedules
from admins.models import Admins
import json
import csv
import datetime

# Create your views here.

class ScoresIndex(ListView):
    model = Scores


class ScoresClassIndex(ListView):
    model = Scores
    
    def get_queryset(self) -> QuerySet[Any]:
        return Scores.objects.filter(student_class__full_name=self.kwargs.get('class_name'))

def createScore(request, class_name):
    students = Students.objects.filter(student_class__full_name=class_name)
    student_class = get_object_or_404(Classes, full_name=class_name)
    if request.method == "POST":
        for student in students:
            name = request.POST.get(f'name{student.id}')
            value = request.POST.get(f'nilai{student.id}')
            mapel_id = request.GET.get('mapel_id')
            obj, created = Scores.objects.update_or_create(
                student_name_id = name,
                student_class = student_class,
                student_name = student,
                subject_name_id = mapel_id,
                defaults={'pas': value}
            )
            if not created:
                obj.score_count = F("score_count") + 1
                obj.save()
            print(obj, created)
            # print(name, value, mapel_id)
    # classes = Subjects.objects.select_related("subject_class", "subject_teacher", "subject_schedule").filter(subject_teacher=request.user.teachers)
    # data = serializers.serialize("json", Teachers.objects.all())
    # data_json = json.loads(data)
    # test = Teachers.objects.values("teacher_name")
    context={
        # 'classes': classes,
        # 'data': data_json,
        # 'test': test,
        'students': students,
        # 'test': test,
    }
    return render(request, 'scores/scores_form.html',  context)
    return JsonResponse(*data_json)