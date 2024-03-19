from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.
jenis_kelamin = (
    (None, _("Select a gender")),
    ("L", _("Male")),
    ("P", _("Female"))
)

class Teachers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Username"))
    teacher_id = models.IntegerField(default=0, verbose_name=_('Teacher Unique Number (NIY)'))
    teacher_name = models.CharField(max_length=100, verbose_name=_("Teacher Name"))
    teacher_gender = models.CharField(max_length=1, choices=jenis_kelamin, verbose_name=_("Teacher Gender"))
    teacher_address = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Teacher Address"))
    teacher_job = models.CharField(max_length=100, blank=True, verbose_name=_("Teacher Job"))
    teacher_email = models.EmailField(default='smaitalbinaa.ekskul@outlook.com', blank=True, verbose_name=_("Teacher Email"))
    teacher_phone = models.CharField(max_length=20, blank=True, default=0, verbose_name=_("Teacher Phone"))
    teacher_photo = models.ImageField(upload_to='teacher', default='blank-profile.png', blank=True, null=True, help_text="format foto .jpg/.jpeg", verbose_name=_("Teacher Photo"))
    is_active = models.BooleanField(default=True, verbose_name=_("Teacher Active Status"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacher_name

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")
        ordering = ["-updated_at"]
        db_table = "teachers"