from django.test import TestCase
from .models import InventoryStatus, Inventories
from faker import Faker
from pytz import timezone

faker = Faker(['id_ID', 'en_US', 'ar_SA'])

# Create your tests here.

class InventoriesCreateTestCase(TestCase):
    def setUp(self) -> None:
        for _ in range(10):
            status = InventoryStatus.objects.create(
                inventory_status_name = faker.first_name(),
                inventory_borrower = faker.first_name(),
                inventory_borrow_amount = 1,
                inventory_borrow_date = faker.date_time(tzinfo=timezone('Asia/Jakarta')),
                inventory_borrow_purpose = faker.first_name(),
                inventory_is_returned = True,
                inventory_return_date = faker.date_time(tzinfo=timezone('Asia/Jakarta')),
            )

            Inventories.objects.create(
                inventory_name = faker.first_name(),
                inventory_total_amount = 1,
                inventory_available_amount = 2,
                inventory_status = status,
                inventory_price = 1.000,
                inventory_buy_date = faker.date_time(tzinfo=timezone('Asia/Jakarta')),
                inventory_buy_place = faker.first_name(),
            )
        return super().setUp()
    
    def test_numbers_of_querysets(self) -> None:
        """Return total of querysets"""
        total_assessments = Inventories.objects.count()
        self.assertEqual(total_assessments, 10)