from django.test import TestCase
from django.contrib.auth.models import User
from .models import TeachersPresences, TeachersClassPresences
from teachers.models import Teachers
from subjects.models import Subjects
from schedules.models import Schedules, TeacherPresenceSchedules
from grades.models import Classes
from faker import Faker
import random

# Create your tests here.
faker = Faker(['id_ID', 'en_US', 'ar_SA'])
gender=('L','P')
semester=("Ganjil", "Genap")
qualitative_scores = ("A", "B", "C", "D")
presence_type = ("Hadir", "Izin", "Alpha", "Sakit", "Cuti")

class TeachersPresencesCreateTestCase(TestCase):
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
            
            schedule = TeacherPresenceSchedules.objects.create(
                schedule_name = faker.first_name(),
                schedule_day = faker.day_of_week(),
                schedule_duration = faker.time_delta(),
                schedule_time_begin = faker.time(),
                schedule_time_end = faker.time(),
                schedule_type = faker.first_name(),
            )

            TeachersPresences.objects.create(
                teaching_date = faker.date(),
                teaching_schedule = schedule,
                teacher_name = teacher,
                teacher_presence = random.choice(presence_type),
                teacher_photo = faker.file_path(depth=2, category='image'),
                semester = random.choice(semester),
                notes = faker.paragraph(nb_sentences=2),
            )

    def test_numbers_of_querysets(self):
        """Return total of querysets"""
        total_assessments = TeachersPresences.objects.count()
        self.assertEqual(total_assessments, 10)



class TeachersClassPresencesCreateTestCase(TestCase):
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

            classes = Classes.objects.create(
                full_name = faker.first_name(),
                short_name = faker.first_name(),
                alias_name = faker.first_name(),
                homeroom_teacher = teacher
            )
            
            schedule = Schedules.objects.create(
                schedule_name = faker.first_name(),
                schedule_name_alias = faker.first_name(),
                schedule_day = faker.day_of_week(),
                schedule_duration = faker.time_delta(),
                schedule_time_begin = faker.time(),
                schedule_time_end = faker.time(),
                schedule_type = faker.first_name(),
            )

            subject = Subjects.objects.create(
                subject_code = faker.first_name(),
                subject_name = faker.first_name(),
                subject_class = classes,
                subject_teacher = teacher,
                subject_schedule = schedule,
                semester = random.choice(semester),
            )

            TeachersClassPresences.objects.create(
                teaching_date = faker.date(),
                teaching_schedule = schedule,
                subject_name = subject,
                teacher_name = teacher,
                teacher_presence = random.choice(presence_type),
                notes = faker.paragraph(nb_sentences=1),
                semester = random.choice(semester)
            )

    def test_numbers_of_querysets(self):
        """Return total of querysets"""
        total_assessments = TeachersClassPresences.objects.count()
        self.assertEqual(total_assessments, 10)