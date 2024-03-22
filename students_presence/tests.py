from django.test import TestCase
from django.contrib.auth.models import User
from .models import StudentsPresences
from teachers.models import Teachers
from subjects.models import Subjects
from schedules.models import Schedules
from grades.models import Classes
from students.models import Students
from faker import Faker
import random

# Create your tests here.
faker = Faker(['id_ID', 'en_US', 'ar_SA'])
gender=('L','P')
semester=("Ganjil", "Genap")
qualitative_scores = ("A", "B", "C", "D")
presence_type = ("Hadir", "Izin", "Alpha", "Sakit", "Cuti", "Mutasi", "Drop Out")

class StudentsPresencesCreateTestCase(TestCase):
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

            student = Students.objects.create(
                student_nis = i * 1234 * random.random(),
                student_nisn = i * 1234 * random.random(),
                student_name = faker.name(),
                student_class = classes,
                student_gender = random.choice(gender),
                student_address = faker.address(),
                student_birth_place = faker.city(),
                student_birth_date = faker.date(),
                student_email = faker.email(),
                student_phone = faker.phone_number()
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

            StudentsPresences.objects.create(
                learning_date = faker.date(),
                subject_schedule = schedule,
                subject_name = subject,
                student_name = student,
                student_class = classes,
                student_presence = random.choice(presence_type),
                notes = faker.paragraph(nb_sentences=2),
                semester = random.choice(semester)
            )

    def test_numbers_of_querysets(self):
        """Return total of querysets"""
        total_assessments = StudentsPresences.objects.count()
        self.assertEqual(total_assessments, 10)