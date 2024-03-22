from django import forms
from django.utils.translation import gettext as _
from grades.models import Classes
from .models import Classes



class ScoreCreateForm(forms.Form):
    class_name = forms.ChoiceField(choices=Classes.objects.all, required=True, label=_("Class Name"))
    subject_name = forms.ChoiceField(choices=Classes.objects.all, required=True, label=_("Subject Name"))
    assessment_name = forms.ChoiceField(choices=Classes.objects.all, required=True, label=_("Assessment Name"))
    assessment_name = forms.ChoiceField(choices=Classes.objects.all, required=True, label=_("Semester"))