from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from subjects.models import Subjects
from teachers.models import Teachers
from grades.models import Classes

# Create your models here.
semester_choices = (
    ("Ganjil", "Ganjil"),
    ("Genap", "Genap"),
)

assesment_list = (
    (None, _("Select one of assessment list")),
    ("PTS", _("Mid-semester assessment")),
    ("PAS", _("End of semester assessment")),
)

# assesment_types = (
#     (None, _("Select one of assessment types")),
#     ("PG", _("Multiple Choice")),
#     ("Isian Singkat", _("Fill in the Blank")),
#     ("Essay", _("Essay")),
#     ("TTS", _("Crossword")),
#     ("Menjodohkan", _("Word Match")),
# )

class AssessmentsTypes(models.Model):
    assesment_type = models.CharField(max_length=10, choices=assesment_list, verbose_name=_("Assesment Type"))
    assesment_name = models.CharField(max_length=100, verbose_name=_("Assesment Name"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.assesment_name
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Assesment Type")
        verbose_name_plural = _("Assesment Types")
        ordering = ["-updated_at"]
        db_table = "assesment_types"

# LJK
# Lembar Essay
# Kertas Buram / Kertas Coretan
# Tidak Perlu Lembar Jawab (Dikerjakan langsung di Soal)
# Yang lain:

class AssessmentsAnswerSheets(models.Model):
    assesment_answer_sheet = models.CharField(max_length=100, choices=assesment_list, verbose_name=_("Assesment Answer Sheet"))
    assesment_answer_sheet_name = models.CharField(max_length=100, verbose_name=_("Assesment Answer Sheet Name"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.assesment_answer_sheet_name
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Assesment Answer Sheet")
        verbose_name_plural = _("Assesment Answer Sheets")
        ordering = ["-updated_at"]
        db_table = "assesment_answer_sheets"


class AssessmentSchedules(models.Model):
    assesment_type = models.ForeignKey(AssessmentsTypes, on_delete=models.CASCADE, verbose_name=_("Assesment Type"))
    assesment_subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name=_("Assesment Subject"))
    assesment_date = models.DateField(verbose_name=_("Assesment Date"))
    assesment_start_time = models.TimeField(blank=True, null=True, verbose_name=_("Assesment Start Time"))
    assesment_end_time = models.TimeField(blank=True, null=True, verbose_name=_("Assesment End Time"))
    assesment_duration = models.DurationField(blank=True, null=True, verbose_name=_("Assesment Duration"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.assesment_date} {self.assesment_subject} {self.assesment_start_time} - {self.assesment_end_time}"
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Assesment Schedule")
        verbose_name_plural = _("Assesment Schedules")
        ordering = ["assesment_date"]
        db_table = "assesment_schedules"


class Assessments(models.Model):
    assesment_name = models.CharField(max_length=10, choices=assesment_list, verbose_name=_("Assesment Name"))
    assesment_schedule = models.ForeignKey(AssessmentSchedules, on_delete=models.SET_NULL, null=True, verbose_name=_("Assesment Schedule"))
    assesment_teacher = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True, verbose_name=_("Subject Teacher"))
    assesment_subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name=_("Subject"))
    assesment_class = models.ManyToManyField(Classes, verbose_name=_("Assesment Class"))
    assesment_type = models.ManyToManyField(AssessmentsTypes, verbose_name=_("Assesment Type"))
    assesment_answer_sheets = models.ManyToManyField(AssessmentsAnswerSheets, verbose_name=_("Assesment Answer Sheets"))
    assesment_notes = models.TextField(blank=True, null=True, verbose_name=_("Notes"))
    semester = models.CharField(max_length=30, choices=semester_choices, verbose_name=_("Semester"))
    created_by = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Created by"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    question_file_upload = models.FileField(upload_to='assesments/questions', verbose_name=_("Question File Upload"), help_text=_("File format must beetween .pdf or .docx"))
    question_grid_upload = models.FileField(upload_to='assesments/grids', verbose_name=_("Question Grid Upload"), help_text=_("File format must beetween .pdf or .docx"))
    answer_file_upload = models.FileField(upload_to='assesments/questions', verbose_name=_("Answer File Upload"), help_text=_("File format must beetween .pdf or .docx"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.assesment_name
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Assesment")
        verbose_name_plural = _("Assesments")
        ordering = ["-updated_at"]
        db_table = "assesments"