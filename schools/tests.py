from django.test import TestCase
from .models import Schools
from faker import Faker
from pytz import timezone

faker = Faker(['id_ID', 'en_US', 'ar_SA'])

# Create your tests here.

class SchoolsCreateTestCase(TestCase):
    def setUp(self) -> None:
        for i in range(10):
            Schools.objects.create(
                nisn = i,
                school_name = faker.first_name(),
                school_status = faker.first_name(),
                school_email = faker.email(),
                school_contact = faker.first_name(),
                school_address = faker.address()
            )
        return super().setUp()
    
    def test_numbers_of_querysets(self) -> None:
        """Return total of querysets"""
        total_assessments = Schools.objects.count()
        self.assertEqual(total_assessments, 10)
