from django.db import models
from django.db.models import F
from students.models import Students
from subjects.models import Subjects
from grades.models import Classes
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.
qualitative_scores = (
    ("A", "Sangat Baik"),
    ("B", "Baik"),
    ("C", "Cukup"),
    ("D", "Kurang"),
)

semester_choices = (
    ("Ganjil", "Ganjil"),
    ("Genap", "Genap"),
)
class Scores(models.Model):  
    student_name = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name=_("Student Name"))
    student_class = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name=_("Student Class"))
    subject_name = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name=_("Subject Name"))
    score_1 = models.PositiveSmallIntegerField(default=0, verbose_name=_("Daily Assessment 1"))
    score_2 = models.PositiveSmallIntegerField(default=0, verbose_name=_("Daily Assessment 2"))
    score_3 = models.PositiveSmallIntegerField(default=0, verbose_name=_("Daily Assessment 3"))
    score_4 = models.PositiveSmallIntegerField(default=0, verbose_name=_("Daily Assessment 4"))
    score_5 = models.PositiveSmallIntegerField(default=0, verbose_name=_("Daily Assessment 5"))
    score_6 = models.PositiveSmallIntegerField(default=0, verbose_name=_("Daily Assessment 6"))
    score_7 = models.PositiveSmallIntegerField(default=0, verbose_name=_("Daily Assessment 7"))
    score_8 = models.PositiveSmallIntegerField(default=0, verbose_name=_("Daily Assessment 8"))
    score_9 = models.PositiveSmallIntegerField(default=0, verbose_name=_("Daily Assessment 9"))
    score_10 = models.PositiveSmallIntegerField(default=0, verbose_name=_("Daily Assessment 10"))
    pts = models.PositiveSmallIntegerField(default=0, verbose_name=_("Midterm Assessment"))
    pas = models.PositiveSmallIntegerField(default=0, verbose_name=_("End of Semester Assessment"))
    student_temporary_score = models.GeneratedField(
        expression=F("score_1") + F("score_2") + F("score_3") + F("score_4") + F("score_5") + F("score_6") + F("score_7") + F("score_8") + F("score_9") + F("score_10") + (F("pts") * 0.4),
        output_field=models.FloatField(),
        db_persist=True,
        verbose_name=_("Temporary Score")
    )
    student_final_score = models.GeneratedField(
        expression=F("score_1") + F("score_2") + F("score_3") + F("score_4") + F("score_5") + F("score_6") + F("score_7") + F("score_8") + F("score_9") + F("score_10") + (F("pts") * 0.2) + (F("pas") * 0.2),
        output_field=models.FloatField(),
        db_persist=True,
        verbose_name=_("Final Score")
    )
    qualitative_score = models.CharField(max_length=20, choices=qualitative_scores, default=qualitative_scores[0][0], verbose_name=_("Attitude Score"))
    semester = models.CharField(max_length=30, choices=semester_choices, verbose_name=_("Semester"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_name.student_name} {self.student_final_score} {self.semester} {self.academic_year}"


    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Score")
        verbose_name_plural = _("Scores")
        ordering = ["-updated_at"]
        db_table = "scores"