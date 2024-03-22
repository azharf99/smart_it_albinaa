from django.test import TestCase
from django.contrib.auth.models import User
from .models import Duties
from teachers.models import Teachers
from faker import Faker
from pytz import timezone
import random

# Create your tests here.
faker = Faker(['id_ID', 'en_US', 'ar_SA'])
gender = ('L', 'P')

class DutiesCreateTestCase(TestCase):
    def setUp(self):
        for i in range(10):
            
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

            Duties.objects.create(
                teacher = teacher,
                duty_type = faker.first_name(),
                duty_start_date = faker.date_time(tzinfo=timezone('Asia/Jakarta')),
                duty_end_date = faker.date_time(tzinfo=timezone('Asia/Jakarta')),
                duty_file = faker.file_path(depth=3, category='text', extension='pdf'),
            )

    def test_numbers_of_querysets(self):
        """Return total of querysets"""
        total_assessments = Duties.objects.count()
        self.assertEqual(total_assessments, 10)