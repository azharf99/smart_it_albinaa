from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Schools(models.Model):
    nisn = models.CharField(max_length=10, unique=True, verbose_name=_("National School Unique Number (NISN)"))
    school_name = models.CharField(max_length=50, verbose_name=_("School Name"))
    school_status = models.CharField(max_length=20, verbose_name=_("School Status"))
    school_email = models.CharField(max_length=50, verbose_name=_("School Email"))
    school_contact = models.CharField(max_length=20, verbose_name=_("School Contact"))
    school_address = models.CharField(max_length=200, verbose_name=_("School Address"))
    school_website = models.URLField(max_length=100, blank=True, null=True, verbose_name=_("School Website"))
    school_instagram = models.URLField(max_length=100, blank=True, null=True, verbose_name=_("School Instagram"))
    school_facebook = models.URLField(max_length=100, blank=True, null=True, verbose_name=_("School Facebook"))
    school_youtube = models.URLField(max_length=100, blank=True, null=True, verbose_name=_("School Youtube"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.school_name}"

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("School")
        verbose_name_plural = _("Schools")
        ordering = ["-updated_at"]
        db_table = "schools"