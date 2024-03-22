from django.test import TestCase
from django.contrib.auth.models import User
from .models import Classes
from teachers.models import Teachers
from faker import Faker
import random

# Create your tests here.
faker = Faker(['id_ID', 'en_US', 'ar_SA'])

gender=('L','P')

class GradesCreateTestCase(TestCase):
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
                teacher_phone = '0',
            )            

            Classes.objects.create(
                full_name = faker.first_name(),
                short_name = faker.first_name(),
                alias_name = faker.first_name(),
                homeroom_teacher = teacher
            )

    def test_numbers_of_querysets(self):
        """Return total of querysets"""
        total_assessments = Classes.objects.count()
        self.assertEqual(total_assessments, 10)