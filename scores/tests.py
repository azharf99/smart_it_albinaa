from django.test import TestCase
from django.contrib.auth.models import User
from .models import Scores
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

class_full_list = (
    "X-MIPA-A",
    "X-MIPA-B",
    "X-MIPA-C",
    "X-MIPA-D",
    "X-MIPA-E",
    "X-MIPA-F",
    "X-MIPA-G",
    "X-MIPA-H",
    "XI-MIPA-A",
    "XI-MIPA-B",
    "XI-MIPA-C",
    "XI-MIPA-D",
    "XI-MIPA-E",
    "XI-MIPA-F",
    "XI-MIPA-G",
    "XI-MIPA-H",
    "XII-MIPA-A",
    "XII-MIPA-B",
    "XII-MIPA-C",
    "XII-MIPA-D",
    "XII-MIPA-E",
    "XII-MIPA-F",
    "XII-MIPA-G",
    "XII-MIPA-H",
)
class_short_list = {
    "X-MIPA-A": "X-A",
    "X-MIPA-B": "X-B",
    "X-MIPA-C": "X-C",
    "X-MIPA-D": "X-D",
    "X-MIPA-E": "X-E",
    "X-MIPA-F": "X-F",
    "X-MIPA-G": "X-G",
    "X-MIPA-H": "X-H",
    "XI-MIPA-A": "XI-A",
    "XI-MIPA-B": "XI-B",
    "XI-MIPA-C": "XI-C",
    "XI-MIPA-D": "XI-D",
    "XI-MIPA-E": "XI-E",
    "XI-MIPA-F": "XI-F",
    "XI-MIPA-G": "XI-G",
    "XI-MIPA-H": "XI-H",
    "XII-MIPA-A": "XII-A",
    "XII-MIPA-B": "XII-B",
    "XII-MIPA-C": "XII-C",
    "XII-MIPA-D": "XII-D",
    "XII-MIPA-E": "XII-E",
    "XII-MIPA-F": "XII-F",
    "XII-MIPA-G": "XII-G",
    "XII-MIPA-H": "XII-H",
}

class ScoresCreateTestCase(TestCase):
    def setUp(self):
        for i in range(50):

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
            
            class_name = random.choice(class_full_list)
            classes = Classes.objects.create(
                full_name = class_name,
                short_name = class_short_list.get(class_name),
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

            score = Scores.objects.create(
                student_name = student,
                student_class = classes,
                subject_name = subject,
                score_1 = random.randint(1, 100),
                score_2 = random.randint(1, 100),
                score_3 = random.randint(1, 100),
                score_4 = random.randint(1, 100),
                score_5 = random.randint(1, 100),
                score_6 = random.randint(1, 100),
                score_7 = random.randint(1, 100),
                score_8 = random.randint(1, 100),
                score_9 = random.randint(1, 100),
                score_10 = random.randint(1, 100),
                pts = random.randint(1, 100),
                pas = random.randint(1, 100),
                qualitative_score = random.choice(qualitative_scores),
                semester = random.choice(semester)
            )

    def test_numbers_of_querysets(self):
        """Return total of querysets"""
        total_assessments = Scores.objects.count()
        self.assertEqual(total_assessments, 50)
    
    def filter_scores_by_students_class_name(self):
        """Return Scores querysets by students class name"""
        data = Scores.objects.filter(student_class__full_name="X-MIPA-C")
        self.assertIsNotNone(data)
