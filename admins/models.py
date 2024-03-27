from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.
jenis_kelamin = (
    ("L", "Laki-laki"),
    ("P", "Perempuan")
)

class Admins(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Username"))
    admin_id = models.IntegerField(default=0, verbose_name=_('NIY'))
    admin_name = models.CharField(max_length=100, verbose_name=_("Admin Name"))
    admin_gender = models.CharField(max_length=1, choices=jenis_kelamin, verbose_name=_("Admin Gender"))
    admin_address = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Admin Address"))
    admin_job = models.CharField(max_length=100, blank=True, verbose_name=_("Admin Job"))
    admin_email = models.EmailField(default='smaitalbinaa.ekskul@outlook.com', blank=True, verbose_name=_("Admin Email"))
    admin_phone = models.CharField(max_length=30, blank=True, default=0, verbose_name=_("Admin Phone"))
    admin_photo = models.ImageField(upload_to='admin', default='blank-profile.png', blank=True, null=True, help_text="format foto .jpg/.jpeg", verbose_name=_("Admin Photo"))
    is_active = models.BooleanField(default=True, verbose_name=_("Admin Active Status"))
    is_online = models.BooleanField(default=False, verbose_name=_("Admin Online Status"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin_name

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = "Admin"
        verbose_name_plural = "Admins"
        ordering = ["-updated_at"]
        db_table = "admins"