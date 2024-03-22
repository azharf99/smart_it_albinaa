from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.
semester_choices = (
    ("Ganjil", "Ganjil"),
    ("Genap", "Genap"),
)

calendar_types = (
    (None, _("Select calendar type")),
    ("All", _("For All Students")),
    ("X", _("For 10th Grade Students Only")),
    ("XI", _("For 11th Grade Students Only")),
    ("XII", _("For 12th Grade Students Only")),
)


class Calendars(models.Model):
    event_name = models.CharField(max_length=100, verbose_name=_("Event Name"))
    event_start_date = models.DateField(verbose_name=_("Event Start Date"))
    event_end_date = models.DateField(blank=True, null=True, verbose_name=_("Event End Date"))
    calendar_types = models.CharField(max_length=30, choices=calendar_types, verbose_name=_("Calendar Types"))
    semester = models.CharField(max_length=30, choices=semester_choices, verbose_name=_("Semester"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    calendar_notes = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Event Name"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if not self.event_end_date:
            return f"{self.event_name} {self.event_start_date} - End"
        return f"{self.event_name} {self.event_start_date} - {self.event_end_date}"
    
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("calendar Schedule")
        verbose_name_plural = _("calendar Schedules")
        ordering = ["event_start_date"]
        db_table = "calendar_schedules"

