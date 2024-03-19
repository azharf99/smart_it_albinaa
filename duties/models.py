from django.db import models
from teachers.models import Teachers
from django.utils.translation import gettext as _

# Create your models here.
class Duties(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name=_("Teacher"))
    duty_type = models.CharField(max_length=100, verbose_name=_("Duty Type"))
    duty_start_date = models.DateTimeField(verbose_name=_("Duty Start Date"))
    duty_end_date = models.DateTimeField(verbose_name=_("Duty End Date"))
    duty_file = models.FileField(upload_to="duty", blank=True, null=True, help_text="format file .pdf/.docx", verbose_name=_("Duty File"))
    duty_notes = models.TextField(max_length=200, blank=True, null=True, verbose_name=_("Duty Notes"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.teacher.teacher_name} {self.duty_type} {self.duty_start_date}"
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Duty")
        verbose_name_plural = _("Duties")
        ordering = ["-updated_at"]
        db_table = "duties"