from django.test import TestCase
from .models import Schedules, TeacherPresenceSchedules
from faker import Faker
from pytz import timezone

faker = Faker(['id_ID', 'en_US', 'ar_SA'])

# Create your tests here.

class SchedulesCreateTestCase(TestCase):
    def setUp(self) -> None:
        for _ in range(10):
            Schedules.objects.create(
                schedule_name = faker.first_name(),
                schedule_name_alias = faker.first_name(),
                schedule_day = faker.first_name(),
                schedule_duration = faker.time_delta(),
                schedule_time_begin = faker.time(),
                schedule_time_end = faker.time(),
                schedule_type = faker.first_name(),
            )
        return super().setUp()
    
    def test_numbers_of_querysets(self) -> None:
        """Return total of querysets"""
        total_assessments = Schedules.objects.count()
        self.assertEqual(total_assessments, 10)


class TeacherPresenceSchedulesCreateTestCase(TestCase):
    def setUp(self) -> None:
        for _ in range(10):
            TeacherPresenceSchedules.objects.create(
                schedule_name = faker.first_name(),
                schedule_day = faker.first_name(),
                schedule_duration = faker.time_delta(),
                schedule_time_begin = faker.time(),
                schedule_time_end = faker.time(),
                schedule_type = faker.first_name(),
            )
        return super().setUp()
    
    def test_numbers_of_querysets(self) -> None:
        """Return total of querysets"""
        total_assessments = TeacherPresenceSchedules.objects.count()
        self.assertEqual(total_assessments, 10)