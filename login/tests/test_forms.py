from django.test import TestCase, Client
from django.urls import reverse
from login.models import Exercise, ExerciseForm

class ExerciseFormTest(TestCase):
    def test_exerciseform_invalid(self):
        form = ExerciseForm({'title':'Demo',
        'category':'Glutes', 
        'rpe':'9: Very Hard Activity',
        'equipment':'Swiss Ball',
        'reps':'3',
        'time':'not a number',
        'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        })
        self.assertFalse(form.is_valid())


    #TODO: fix the test for a valid form, incorrect response
    # def test_exerciseform_valid(self):
    #     form = ExerciseForm({'title':'Demo',
    #     'category':'Glutes', 
    #     'rpe':'9: Very Hard Activity',
    #     'equipment':'Swiss Ball',
    #     'reps':'12',
    #     'time':'not a number',
    #     'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    #     })
    #     self.assertTrue(form.is_valid)