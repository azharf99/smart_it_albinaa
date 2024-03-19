from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from teachers.models import Teachers
from grades.models import Classes
from schedules.models import Schedules

# Create your models here.
semester_choices = (
    ("Ganjil", "Ganjil"),
    ("Genap", "Genap"),
)
class Subjects(models.Model):
    subject_code = models.CharField(max_length=100, verbose_name=_("Subject Code"))
    subject_name = models.CharField(max_length=100, verbose_name=_("Subject Name"))
    subject_class = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, verbose_name=_("Subject Class"))
    subject_teacher = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True, verbose_name=_("Subject Teacher"))
    subject_schedule = models.ForeignKey(Schedules, on_delete=models.SET_NULL, null=True, verbose_name=_("Subject Schedule"))
    semester = models.CharField(max_length=30, choices=semester_choices, verbose_name=_("Semester"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject_name} {self.subject_class} {self.subject_teacher}"

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")
        ordering = ["-updated_at"]
        db_table = "subjects"