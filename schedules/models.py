from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.
# pilihan_jam_kbm_normal = (
#     ("1", "Jam ke - 1"),
#     ("2", "Jam ke - 2"),
#     ("3", "Jam ke - 3"),
#     ("4", "Jam ke - 4"),
#     ("5", "Jam ke - 5"),
#     ("6", "Jam ke - 6"),
#     ("7", "Jam ke - 7"),
#     ("8", "Jam ke - 8"),
#     ("9", "Jam ke - 9"),
# )

day_choices=(
    (None, _("Select schedule day")),
    ("Monday", _("Monday")),
    ("Tuesday", _("Tuesday")),
    ("Wednesday", _("Wednesday")),
    ("Thursday", _("Thursday")),
    ("Friday", _("Friday")),
    ("Saturday", _("Saturday")),
    ("Sunday", _("Sunday")),
)

class Schedules(models.Model):
    schedule_name = models.CharField(max_length=20, verbose_name=_("Schedule Name"))
    schedule_name_alias = models.CharField(max_length=20, verbose_name=_("Schedule Alias Name"))
    schedule_day = models.CharField(max_length=20, choices=day_choices, verbose_name=_("Schedule Day"))
    schedule_duration = models.DurationField(max_length=20, verbose_name=_("Schedule Duration"))
    schedule_time_begin = models.TimeField(verbose_name=_("Schedule Start Time"))
    schedule_time_end = models.TimeField(verbose_name=_("Schedule End Time"))
    schedule_type = models.CharField(max_length=20, verbose_name=_("Schedule Type"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.schedule_name_alias} {self.schedule_duration}"
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Schedule")
        verbose_name_plural = _("Schedules")
        ordering = ["-updated_at"]
        db_table = "schedules"


class TeacherPresenceSchedules(models.Model):
    schedule_name = models.CharField(max_length=20, verbose_name=_("Schedule Name"))
    schedule_day = models.CharField(max_length=20, choices=day_choices, verbose_name=_("Schedule Day"))
    schedule_duration = models.DurationField(max_length=20, verbose_name=_("Schedule Duration"))
    schedule_time_begin = models.TimeField(verbose_name=_("Schedule Start Time"))
    schedule_time_end = models.TimeField(verbose_name=_("Schedule End Time"))
    schedule_type = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name=_("Schedule Type"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.schedule_day} {self.schedule_duration}"
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Teacher presence schedule")
        verbose_name_plural = _("Teacher presence schedules")
        ordering = ["-updated_at"]
        db_table = "teacher_presence_schedules"