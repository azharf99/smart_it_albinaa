from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.
class Proposals(models.Model):
    proposal_name = models.CharField(max_length=200, verbose_name=_("Proposal Name"))
    proposal_start_date_execution = models.DateField(verbose_name=_("Proposal Start Date Execution"))
    proposal_end_date_execution = models.DateField(blank=True, null=True, verbose_name=_("Proposal End Date Execution"))
    proposal_purpose = models.CharField(max_length=200, verbose_name=_("Proposal Purpose"))
    proposal_pic = models.CharField(max_length=200, verbose_name=_("Proposal Person In Charge"))
    proposal_pic_bank_account = models.CharField(max_length=100, default="Muamalat", verbose_name=_("Proposal Person In Charge Bank Account"))
    proposal_pic_account_number = models.CharField(max_length=100, default="", verbose_name=_("Proposal Person In Charge Account Number"))
    proposal_estimated_cost_budget = models.FloatField(verbose_name=_("Estimated Cost Budget"))
    proposal_notes = models.TextField(blank=True, null=True, verbose_name=_("Notes"))
    created_by = models.CharField(blank=True, null=True, verbose_name=_("Created by"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    proposal_file_upload = models.FileField(upload_to='proposals', verbose_name=_("Proposal File Upload"), help_text=_("File format must beetween .pdf or .docx"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.proposal_name[:15]
    

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Proposal")
        verbose_name_plural = _("Proposals")
        ordering = ["-updated_at"]
        db_table = "proposals"