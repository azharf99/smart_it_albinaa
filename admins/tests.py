from django.test import TestCase
from django.contrib.auth.models import User
from .models import Admins
from faker import Faker
import random

# Create your tests here.
faker = Faker(['id_ID', 'en_US', 'ar_SA'])
gender=('L','P')

class AdminCreateTestCase(TestCase):
    def setUp(self):
        for _ in range(100):
            name = faker.unique.first_name()
            user = User.objects.create(
                username = name.lower(),
                password = "Azhar1995",
                first_name = name,
                last_name = faker.last_name(),
                email = faker.email()
            )
            Admins.objects.create(
                user = user,
                admin_name = faker.name(),
                admin_gender = random.choice(gender),
                admin_address = faker.address(),
                admin_job = faker.job(),
                admin_email = faker.email(),
                admin_phone = faker.phone_number(),
            )
    def test_numbers_of_querysets(self):
        """Return total of querysets"""
        total_user = User.objects.all().count()
        total_admin = Admins.objects.all().count()
        self.assertEqual(total_user, 100)
        self.assertEqual(total_admin, 100)