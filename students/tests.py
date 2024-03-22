from django.test import TestCase
from django.contrib.auth.models import User
from .models import Students, StudentParents
from teachers.models import Teachers
from grades.models import Classes
from faker import Faker
import random

# Create your tests here.
faker = Faker(['id_ID', 'en_US', 'ar_SA'])
gender=('L','P')
semester=("Ganjil", "Genap")
qualitative_scores = ("A", "B", "C", "D")

class StudentsCreateTestCase(TestCase):
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

            Students.objects.create(
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

    def test_numbers_of_querysets(self):
        """Return total of querysets"""
        total_assessments = Students.objects.count()
        self.assertEqual(total_assessments, 10)


class StudentParentsCreateTestCase(TestCase):
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

            StudentParents.objects.create(
                student_name = student,
                student_birth_order = random.randint(1, 10),
                student_dad_name = faker.name(),
                student_dad_job = faker.job(),
                student_dad_phone = faker.phone_number(),
                student_dad_email = faker.email(),
                student_dad_education = faker.company(),
                student_mom_name = faker.name(),
                student_mom_job = faker.job(),
                student_mom_education = faker.company(),
                student_mom_phone = faker.phone_number(),
                student_mom_email = faker.email(),
                student_guardian_name = faker.name(),
                student_guardian_address = faker.address(),
                student_guardian_phone = faker.phone_number(),
                student_guardian_email = faker.email(),
            )

    def test_numbers_of_querysets(self):
        """Return total of querysets"""
        total_assessments = StudentParents.objects.count()
        self.assertEqual(total_assessments, 10)