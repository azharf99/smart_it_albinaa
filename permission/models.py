from django.db import models
from teachers.models import Teachers
from django.utils.translation import gettext as _
# Create your models here.
tipe_perizinan = (
    ("Izin", _("Izin")),
    ("Sakit", _("Sakit")),
    ("Cuti", _("Cuti")),
)

class Permission(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name=_("Teacher"))
    permission_type = models.CharField(max_length=20, choices=tipe_perizinan, verbose_name=_("Permission Type"))
    permission_start_date = models.DateTimeField(verbose_name=_("Permission Start Date"))
    permission_end_date = models.DateTimeField(verbose_name=_("Permission End Date"))
    permission_file = models.FileField(upload_to="permission", blank=True, null=True, help_text="format file .pdf/.docx", verbose_name=_("Permission File"))
    permission_notes = models.TextField(max_length=200, blank=True, null=True, verbose_name=_("Permission Notes"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.teacher.teacher_name} {self.permission_type} {self.permission_start_date}"
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Permission")
        verbose_name_plural = _("Permissions")
        ordering = ["-updated_at"]
        db_table = "permissions"