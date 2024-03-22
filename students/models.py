from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from grades.models import Classes

# Create your models here.

jenis_kelamin = (
    (None, _("Select a gender")),
    ("L", _("Male")),
    ("P", _("Female"))
)

class Students(models.Model):
    student_nis = models.CharField(max_length=20, unique=True, verbose_name=_("Student's Unique Number (NIS)"))
    student_nisn = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("National Student's Unique Number (NISN)"))
    student_name = models.CharField(max_length=100, verbose_name=_("Student Name"))
    student_class = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, verbose_name=_("Student's Class"))
    student_gender = models.CharField(max_length=10, choices=jenis_kelamin, verbose_name=_("Student's Gender"))
    student_address = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Student's Address"))
    student_birth_place = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Student's Birth Place"))
    student_birth_date = models.DateField(blank=True, null=True, verbose_name=_("Student's Birth Date"))
    student_email = models.EmailField(max_length=50, blank=True, null=True, verbose_name=_("Student's Email"))
    student_phone = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Student's Phone"))
    student_status = models.CharField(max_length=50, blank=True, default="Aktif", verbose_name=_("Student's Status"))
    student_photo = models.ImageField(upload_to='student', blank=True, null=True, default='blank-profile.png', help_text="Format foto .jpg/.jpeg", verbose_name=_("Student's Photo"))
    student_batch = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_("Student's Batch"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_name} {self.student_name} {self.student_batch} {self.academic_year}"

    class Meta:
        indexes = [
            models.Index(fields=["student_nis", "id",]),
        ]
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
        ordering = ["student_class", "student_name"]
        db_table = "students"



class StudentParents(models.Model):
    student_name = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name=_("Student's Name"))
    student_birth_order = models.PositiveSmallIntegerField(default=1, verbose_name=_("Student's Birth Order"))
    student_dad_name = models.CharField(max_length=100, verbose_name=_("Student's Dad Name"))
    student_dad_job = models.CharField(max_length=100, verbose_name=_("Student's Dad Job"))
    student_dad_phone = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Student's Dad Phone"))
    student_dad_email = models.EmailField(max_length=100, blank=True, null=True, verbose_name=_("Student's Dad Email"))
    student_dad_education = models.CharField(max_length=100, verbose_name=_("Student's Dad Education"))
    student_mom_name = models.CharField(max_length=100, verbose_name=_("Student's Mom Name"))
    student_mom_job = models.CharField(max_length=100, verbose_name=_("Student's Mom Job"))
    student_mom_education = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Student's Mom Education"))
    student_mom_phone = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Student's Mom Phone"))
    student_mom_email = models.EmailField(max_length=100, blank=True, null=True, verbose_name=_("Student's Mom Email"))
    student_guardian_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Student's Guardian Name"))
    student_guardian_address = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Student's Guardian Address"))
    student_guardian_phone = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Student's Guardian Phone"))
    student_guardian_email = models.EmailField(max_length=100, blank=True, null=True, verbose_name=_("Student's Guardian Email"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_name}"

    class Meta:
        indexes = [
            models.Index(fields=["id",]),
        ]
        verbose_name = _("Student's Parent")
        verbose_name_plural = _("Student's Parents")
        ordering = ["student_name"]
        db_table = "student_parents"