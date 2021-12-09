from django.test import TestCase
from login.models import Exercise, ExerciseForm, Reminder, ReminderForm
from django.conf import settings
import unittest
from django.contrib.auth import get_user_model
import datetime
from django.utils import timezone

User = get_user_model()

class ExerciseModel(unittest.TestCase):
    def setUp(self):
        my_user = User.objects.get(pk=1)
        Exercise.objects.create(title='Test', category='Glutes',rpe='9: Very Hard Activity',equipment='Swiss Ball',reps='3',time='60',description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', points=10, user=my_user)
    
    def test_title_label(self):
        self.exercise = Exercise.objects.get(title='Test')
        field_label = self.exercise._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        
    def test_category_label(self):
        self.exercise = Exercise.objects.get(title='Test')
        field_label = self.exercise._meta.get_field('category').verbose_name
        self.assertEqual(field_label,'category')
        
    def test_rpe_label(self):
        self.exercise = Exercise.objects.get(title='Test')
        field_label = self.exercise._meta.get_field('rpe').verbose_name
        self.assertEqual(field_label,'rpe')

    def test_equipment_label(self):
        self.exercise = Exercise.objects.get(title='Test')
        field_label = self.exercise._meta.get_field('equipment').verbose_name
        self.assertEqual(field_label,'equipment')

    def test_reps_label(self):
        self.exercise = Exercise.objects.get(title='Test')
        field_label = self.exercise._meta.get_field('reps').verbose_name
        self.assertEqual(field_label,'reps')
    
    def test_time_label(self):
        self.exercise = Exercise.objects.get(title='Test')
        field_label = self.exercise._meta.get_field('time').verbose_name
        self.assertEqual(field_label,'time')

    def test_description_label(self):
        self.exercise = Exercise.objects.get(title='Test')
        field_label = self.exercise._meta.get_field('description').verbose_name
        self.assertEqual(field_label,'description')

    def test_title_max_length(self):
        self.exercise = Exercise.objects.get(title='Test')
        max_length = self.exercise._meta.get_field('title').max_length
        self.assertEqual(max_length, 60)
        
    def test_category_max_length(self):
        self.exercise = Exercise.objects.get(title='Test')
        max_length = self.exercise._meta.get_field('category').max_length
        self.assertEqual(max_length, 60)
    
    def test_rpe_max_length(self):
        self.exercise = Exercise.objects.get(title='Test')
        max_length = self.exercise._meta.get_field('rpe').max_length
        self.assertEqual(max_length, 60)

    def test_equipment_max_length(self):
        self.exercise = Exercise.objects.get(title='Test')
        max_length = self.exercise._meta.get_field('equipment').max_length
        self.assertEqual(max_length, 60)

    def test_description_max_length(self):
        self.exercise = Exercise.objects.get(title='Test')
        max_length = self.exercise._meta.get_field('description').max_length
        self.assertEqual(max_length, 1500)

    def tearDown(self):
        self.exercise.delete()
        
class ReminderModel(unittest.TestCase):
    def setUp(self):
        my_user = User.objects.get(pk=1)
        d = datetime.time(10, 33, 45)
        Reminder.objects.create(title='Reminder Test', time_days=10, time_hours=9, time_minutes=30, time_now=d, description='Reminder!', user=my_user)
    
    def test_title_label(self):
        self.reminder = Reminder.objects.get(title='Reminder Test')
        field_label = self.reminder._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
    
    def test_time_hours_label(self):
        self.reminder = Reminder.objects.get(title='Reminder Test')
        field_label = self.reminder._meta.get_field('time_hours').verbose_name
        self.assertEqual(field_label,'time hours')
        
    def test_time_days_label(self):
        self.reminder = Reminder.objects.get(title='Reminder Test')
        field_label = self.reminder._meta.get_field('time_days').verbose_name
        self.assertEqual(field_label,'time days')
        
    def test_time_minutes_label(self):
        self.reminder = Reminder.objects.get(title='Reminder Test')
        field_label = self.reminder._meta.get_field('time_minutes').verbose_name
        self.assertEqual(field_label,'time minutes')

    def test_description_label(self):
        self.reminder = Reminder.objects.get(title='Reminder Test')
        field_label = self.reminder._meta.get_field('description').verbose_name
        self.assertEqual(field_label,'description')

    def test_title_max_length(self):
        self.reminder = Reminder.objects.get(title='Reminder Test')
        max_length = self.reminder._meta.get_field('title').max_length
        self.assertEqual(max_length, 60)

    def test_description_max_length(self):
        self.reminder = Reminder.objects.get(title='Reminder Test')
        max_length = self.reminder._meta.get_field('description').max_length
        self.assertEqual(max_length, 1500)

    def tearDown(self):
        self.reminder.delete()