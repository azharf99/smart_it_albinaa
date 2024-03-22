from django.test import TestCase
from django.contrib.auth.models import User
from teachers.models import Teachers
from .models import Permits
from faker import Faker
from pytz import timezone
import random

faker = Faker(['id_ID', 'en_US', 'ar_SA'])

# Create your tests here.
gender = ('L', 'P')
class PermitsCreateTestCase(TestCase):
    def setUp(self) -> None:
        for _ in range(10):
            name = faker.unique.first_name()
            user = User.objects.create(
                username = name.lower(),
                password = "Azhar1995",
                first_name = name,
                last_name = faker.last_name(),
                email = faker.email()
            )
            
            teacher = Teachers.objects.create(
                user = user,
                teacher_name = faker.name(),
                teacher_gender = random.choice(gender),
                teacher_address = faker.address(),
                teacher_job = faker.job(),
                teacher_email = faker.email(),
                teacher_phone = faker.phone_number(),
            )

            Permits.objects.create(
                teacher = teacher,
                permit_type = 1,
                permit_start_date = faker.date_time(tzinfo=timezone('Asia/Jakarta')),
                permit_end_date = faker.date_time(tzinfo=timezone('Asia/Jakarta')),
                permit_file = faker.file_path(depth=3, category='text', extension='pdf'),

            )
        return super().setUp()
    
    def test_numbers_of_querysets(self) -> None:
        """Return total of querysets"""
        total_assessments = Permits.objects.count()
        self.assertEqual(total_assessments, 10)