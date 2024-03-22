from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from subjects.models import Subjects
from teachers.models import Teachers
from schedules.models import Schedules, TeacherPresenceSchedules

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

class TeachersPresences(models.Model):
    teaching_date = models.DateField(default=timezone.now, verbose_name=_("Teaching Date"))
    teaching_schedule = models.ForeignKey(TeacherPresenceSchedules, on_delete=models.SET_NULL, null=True, verbose_name=_("Teaching Schedule"))
    teacher_name = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name=_("Teacher Name"))
    teacher_presence = models.CharField(max_length=30, choices=presence_types, verbose_name=_("Teacher Presence"), default=presence_types[0][0])
    teacher_photo = models.ImageField(upload_to='presences', help_text="Pastikan foto jelas/tidak blur", verbose_name=_("Teacher Photo"))
    semester = models.CharField(max_length=30, choices=semester_choices, verbose_name=_("Semester"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    notes = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.teaching_date} {self.teacher_name}"
    
    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Teachers Presence")
        verbose_name_plural = _("Teachers Presences")
        ordering = ["-updated_at"]
        db_table = "teachers_presences"


class TeachersClassPresences(models.Model):
    teaching_date = models.DateField(default=timezone.now, verbose_name=_("Teaching Date"))
    teaching_schedule = models.ForeignKey(Schedules, on_delete=models.SET_NULL, null=True, verbose_name=_("Teaching Schedule"))
    subject_name = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name=_("Subject Name"))    
    teacher_name = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name=_("Teacher Name"))    
    teacher_presence = models.CharField(max_length=30, choices=presence_types, verbose_name=_("Teacher Presence"), default=presence_types[0][0])
    semester = models.CharField(max_length=30, choices=semester_choices, verbose_name=_("Semester"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    notes = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.teaching_date} {self.teacher_name}"
    
    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Teachers Class Presence")
        verbose_name_plural = _("Teachers Class Presences")
        ordering = ["-updated_at"]
        db_table = "teachers_class_presences"