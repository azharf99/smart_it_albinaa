from django.db import models
from django.contrib.auth.models import User

# Create your models here.
jenis_kelamin = (
    ("L", "Laki-laki"),
    ("P", "Perempuan")
)

class Admins(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Username")
    admin_id = models.IntegerField(default=0, verbose_name='NIY')
    admin_name = models.CharField(max_length=100, verbose_name="Admin name")
    admin_gender = models.CharField(max_length=1, choices=jenis_kelamin)
    admin_address = models.CharField(max_length=100, blank=True, null=True)
    admin_job = models.CharField(max_length=100, blank=True)
    admin_email = models.EmailField(default='smaitalbinaa.ekskul@outlook.com', blank=True)
    admin_phone = models.CharField(max_length=20, blank=True, default=0)
    admin_photo = models.ImageField(upload_to='admin', default='blank-profile.png', blank=True, null=True, help_text="format foto .jpg/.jpeg")
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