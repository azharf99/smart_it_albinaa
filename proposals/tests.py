from django.test import TestCase
from django.contrib.auth.models import User
from teachers.models import Teachers
from .models import Proposals
from faker import Faker
from pytz import timezone
import random

faker = Faker(['id_ID', 'en_US', 'ar_SA'])

# Create your tests here.
class ProposalsCreateTestCase(TestCase):
    def setUp(self) -> None:
        for _ in range(10):

            Proposals.objects.create(
                proposal_name = faker.name(),
                proposal_start_date_execution = faker.date(),
                proposal_end_date_execution = faker.date(),
                proposal_purpose = faker.name(),
                proposal_pic = faker.name(),
                proposal_pic_bank_account = faker.first_name(),
                proposal_pic_account_number = faker.aba(),
                proposal_estimated_cost_budget = 1000 * random.random(),
                proposal_file_upload = faker.file_path(depth=3, category='text', extension='pdf'),

            )
        return super().setUp()
    
    def test_numbers_of_querysets(self) -> None:
        """Return total of querysets"""
        total_assessments = Proposals.objects.count()
        self.assertEqual(total_assessments, 10)