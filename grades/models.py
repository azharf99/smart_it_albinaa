from django.db import models
from teachers.models import Teachers
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.
class Classes(models.Model):
    full_name = models.CharField(max_length=20, verbose_name=_("Class Full Name"))
    short_name = models.CharField(max_length=20, verbose_name=_("Class Short Name"))
    alias_name = models.CharField(max_length=80, blank=True, null=True,  verbose_name=_("Class Alias Name"))
    homeroom_teacher = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True, verbose_name=_("Homeroom Teacher"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.full_name} T.A. {self.academic_year}"

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")
        ordering = ["-updated_at"]
        db_table = "classes"
