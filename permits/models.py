from django.db import models
from teachers.models import Teachers
from django.utils.translation import gettext as _
# Create your models here.
tipe_perizinan = (
    ("Izin", _("Izin")),
    ("Sakit", _("Sakit")),
    ("Cuti", _("Cuti")),
)

class Permits(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name=_("Teacher"))
    permit_type = models.CharField(max_length=20, choices=tipe_perizinan, verbose_name=_("Permit Type"))
    permit_start_date = models.DateTimeField(verbose_name=_("Permit Start Date"))
    permit_end_date = models.DateTimeField(verbose_name=_("Permit End Date"))
    permit_file = models.FileField(upload_to="Permit", blank=True, null=True, help_text="format file .pdf/.docx", verbose_name=_("Permit File"))
    permit_notes = models.TextField(max_length=200, blank=True, null=True, verbose_name=_("Permit Notes"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.teacher.teacher_name} {self.permit_type} {self.permit_start_date}"
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Permit")
        verbose_name_plural = _("Permits")
        ordering = ["-updated_at"]
        db_table = "permits"