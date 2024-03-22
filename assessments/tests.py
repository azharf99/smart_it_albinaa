from django.test import TestCase
from django.contrib.auth.models import User
from .models import Assessments, AssessmentsAnswerSheets, AssessmentSchedules, AssessmentsTypes
from teachers.models import Teachers
from subjects.models import Subjects
from schedules.models import Schedules
from grades.models import Classes
from faker import Faker
import random

# Create your tests here.
faker = Faker(['id_ID', 'en_US', 'ar_SA'])
assesment_list=(
    ('PTS','PAS'), 
     {
        'PTS': "Mid-semester assessment", 
        'PAS': "End of semester assessment"
     }
    )
assesment_answer_sheets_list=(
    ('LJK','Essay','Kertas Buram','Tidak perlu','Lainnya'), 
     {
        'LJK': "Lembar Jawaban Komputer", 
        'Essay': "Lembar Essay",
        'Kertas Buram': "Kertas Buram/Kertas Coretan",
        'Tidak perlu': "Tidak Perlu Lembar Jawab (Dikerjakan langsung di Soal)",
        'Lainnya': "Lainnya"
     }
    )

gender=('L','P')
semester=("Ganjil", "Genap")

class AssessmentsCreateTestCase(TestCase):
    def setUp(self):
        for i in range(10):
            assesment_type = random.choice(assesment_list[0])
            assesment_answers = random.choice(assesment_answer_sheets_list[0])

            assesment_types = AssessmentsTypes.objects.create(
                assesment_type = assesment_type,
                assesment_name = assesment_list[1].get(assesment_type)
            )

            assesment_answer_sheets = AssessmentsAnswerSheets.objects.create(
                assesment_answer_sheet = assesment_answers,
                assesment_answer_sheet_name = assesment_answer_sheets_list[1].get(assesment_answers)
            )

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

            assessment_schedules = AssessmentSchedules.objects.create(
                assesment_type = assesment_types,
                assesment_subject = subject,
                assesment_date = faker.date(),
                assesment_start_time = faker.time(),
                assesment_end_time = faker.time(),
                assesment_duration = faker.time_delta()
            )

            assesment = Assessments(
                id = i+1,
                assesment_name = 'PTS',
                assesment_schedule = assessment_schedules,
                assesment_teacher = teacher,
                assesment_subject = subject,
                semester = random.choice(semester),
                question_file_upload = faker.file_path(depth=3, category='text', extension='pdf'),
                question_grid_upload = faker.file_path(depth=3, category='text', extension='pdf'),
                answer_file_upload = faker.file_path(depth=3, category='text', extension='pdf')
            )

            assesment.assesment_class.add(classes)
            assesment.assesment_type.add(assesment_types)
            assesment.assesment_answer_sheets.add(assesment_answer_sheets)

            assesment.save()
    def test_numbers_of_querysets(self):
        """Return total of querysets"""
        total_assessments = Assessments.objects.count()
        self.assertEqual(total_assessments, 10)