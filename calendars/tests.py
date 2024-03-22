from django.test import TestCase
from .models import Calendars
from faker import Faker
import random

# Create your tests here.
faker = Faker(['id_ID', 'en_US', 'ar_SA'])

calendar_types = ("All", "X", "XI", "XII")
semester=("Ganjil", "Genap")

class CalendarsCreateTestCase(TestCase):
    def setUp(self):
        for _ in range(10):
            Calendars.objects.create(
                event_name = faker.first_name(),
                event_start_date = faker.date(),
                event_end_date = faker.date(),
                calendar_types = random.choice(calendar_types),
                semester = random.choice(semester),
            )
    def test_numbers_of_querysets(self):
        """Return total of querysets"""
        total_assessments = Calendars.objects.count()
        self.assertEqual(total_assessments, 10)