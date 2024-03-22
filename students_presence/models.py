from django.db import models
from students.models import Students
from grades.models import Classes
from subjects.models import Subjects
from schedules.models import Schedules
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.
presence_types = (
    ("Hadir", _("Hadir")),
    ("Izin", _("Izin")),
    ("Sakit", _("Sakit")),
    ("Alpha", _("Tanpa Keterangan")),
    ("Cuti", _("Cuti")),
)

semester_choices = (
    ("Ganjil", "Ganjil"),
    ("Genap", "Genap"),
)

class StudentsPresences(models.Model):
    learning_date = models.DateField(default=timezone.now, verbose_name=_("Lesson Date"))
    subject_schedule = models.ForeignKey(Schedules, on_delete=models.SET_NULL, null=True, verbose_name=_("Subject Schedule"))
    subject_name = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name=_("Subject Name"))
    student_name = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name=_("Student Name"))
    student_class = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name=_("Student Class"))
    student_presence = models.CharField(max_length=20, choices=presence_types, default=presence_types[0][0], verbose_name=_("Student Presence"))
    notes = models.CharField(max_length=250, blank=True, verbose_name=_("Notes"))
    semester = models.CharField(max_length=30, choices=semester_choices, verbose_name=_("Semester"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.learning_date} {self.student_class} {self.student_name}"
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Students Presence")
        verbose_name_plural = _("Students Presences")
        ordering = ["-updated_at"]
        db_table = "students_presences"
