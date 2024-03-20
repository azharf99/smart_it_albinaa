from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.
class Inventories(models.Model):
    inventory_name = models.CharField(max_length=100, verbose_name=_("Inventory Name"))
    inventory_total_amount = models.PositiveIntegerField(default=1, verbose_name=_("Inventory Total Amount"))
    inventory_available_amount = models.PositiveIntegerField(default=1, verbose_name=_("Inventory Available Amount"))
    inventory_owner = models.CharField(max_length=100, default="SMAS IT AL BINAA", verbose_name=_("Inventory Owner"))
    inventory_status = models.ForeignKey("InventoryStatus", on_delete=models.CASCADE, verbose_name=_("Inventory Status"))
    inventory_price = models.FloatField(blank=True, verbose_name=_("Inventory Price"))
    inventory_buy_date = models.DateTimeField(blank=True, null=True, verbose_name=_("Inventory Buy Date"))
    inventory_buy_place = models.CharField(max_length=100, blank=True, verbose_name=_("Inventory Buy Place"))
    inventory_notes = models.TextField(max_length=200, blank=True, null=True, verbose_name=_("Notes"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.inventory_name}"

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Inventory")
        verbose_name_plural = _("Inventories")
        ordering = ["-updated_at"]
        db_table = "inventories"
        


class InventoryStatus(models.Model):
    inventory_name = models.ForeignKey(Inventories, on_delete=models.CASCADE)
    inventory_borrower = models.CharField(max_length=100)
    inventory_borrow_amount = models.PositiveSmallIntegerField()
    inventory_borrow_date = models.DateTimeField(auto_now_add=True)
    inventory_borrow_purpose = models.CharField(max_length=100)
    inventory_borrow_notes = models.TextField(max_length=200, blank=True, null=True)
    inventory_is_returned = models.BooleanField(default=False)
    inventory_return_date = models.DateTimeField(blank=True, null=True)
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.inventory_name} {self.inventory_borrower}"

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Inventory Status")
        verbose_name_plural = _("Inventory Statuses")
        ordering = ["-updated_at"]
        db_table = "inventory_status"