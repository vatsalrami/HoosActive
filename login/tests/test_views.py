from django.test import TestCase, Client
from django.urls import reverse
from login.models import Exercise, ExerciseForm, Reminder, ReminderForm

#TODO: test exercise view form


class ExercisesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.exercises_url = reverse('exercises')
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('exercises'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(self.exercises_url)
        self.assertEqual(response.status_code,200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(self.exercises_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'login/exercise_list.html')
        
class ReminderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.reminders_url = reverse('reminders')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('reminders'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(self.reminders_url)
        self.assertEqual(response.status_code,200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(self.reminders_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'login/reminder_list.html')

class CalendarViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.calendar_url = reverse('calendar')
        
    def test_calendar_url_exists_at_desired_location(self):
        response = self.client.get(reverse('calendar'))
        self.assertEqual(response.status_code, 200)
    
    def test_calendar_url_accessible_by_name(self):
        response = self.client.get(self.calendar_url)
        self.assertEqual(response.status_code,200)
        
class LeaderboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.leaderboard_url = reverse('leaderboard')
    
    def test_leaderboard_url_exists_at_desired_location(self):
        response = self.client.get(reverse('leaderboard'))
        self.assertEqual(response.status_code, 200)
    
    def test_leaderboard_url_accessible_by_name(self):
        response = self.client.get(self.leaderboard_url)
        self.assertEqual(response.status_code,200)