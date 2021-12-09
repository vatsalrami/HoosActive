from django.db import models
from django import forms
import datetime
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

#TODO: make migrations for updated rpe choices
RPE_CHOICES = (
    ('1: Resting','1: Resting'),
    ('2: Minimum Activity','2: Minimum Activity'),
    ('3-4: Light Activity','3-4: Light Activity'),
    ('5-6: Moderate Activity','5-6: Moderate Activity'),
    ('7-8: Hard Activity','7-8: Hard Activity'),
    ('9: Very Hard Activity','9: Very Hard Activity'),
    ('10: Maximal Exertion','10: Maximal Exertion'),
    )
CATEG_CHOICES = (
    ('Arms','Arms'),
    ('Abs','Abs'),
    ('Chest','Chest'),
    ('Back','Back'),
    ('Legs','Legs'),
    ('Glutes','Glutes'),
    ('Shoulders','Shoulders'),
)
EQUIP_CHOICES = (
    ('Barbell','Barbell'),
    ('Bench','Bench'),
    ('Dumbbell','Dumbbell'),
    ('Gym Mat','Gym Mat'),
    ('Incline Bench','Incline Bench'),
    ('Kettlebell','Kettlebell'),
    ('Pull-Up Bar','Pull-Up Bar'),
    ('SZ-Bar','SZ-Bar'),
    ('Swiss Ball','Swiss Ball'),
    ('Rowing Machine','Rowing Machine'),
    ('Exercise Ball','Exercise Ball'),
    ('Stationary Bikes','Stationary Bikes'),
    ('Ellipticals','Ellipticals'),
    ('Treadmill','Treadmill'),
    ('None','None'),
)
#TODO: create function to append choices to equipment tuple
#TODO: include add equipment button separate from dropdown list

User = settings.AUTH_USER_MODEL

class Exercise(models.Model):
    title = models.CharField(max_length=60, primary_key=True)
    category = models.CharField(max_length=60, choices=CATEG_CHOICES, null=True)
    rpe = models.CharField(max_length=60, choices=RPE_CHOICES, null=True)
    equipment = models.CharField(max_length=60, choices=EQUIP_CHOICES, null=True )
    reps = models.PositiveIntegerField()
    time = models.PositiveIntegerField()
    description = models.TextField(max_length=1500)
    points = models.PositiveIntegerField()
    user = models.ForeignKey(User, default = 1, null = True, on_delete = models.SET_NULL)
    def __str__(self):
        return '%s %s %s %s %d %d %s' % (self.title, self.category, self.rpe, self.equipment, self.reps, self.time, self.description)

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['title', 'category', 'rpe', 'equipment', 'reps', 'time', 'description']

class Reminder(models.Model):
    title = models.CharField(max_length=60, primary_key=True)
    time_days = models.PositiveIntegerField(default="")
    time_hours = models.PositiveIntegerField()
    time_minutes = models.PositiveIntegerField()
    time_now = models.DateTimeField(auto_now=True, null=True)
    description = models.TextField(max_length=1500)
    user = models.ForeignKey(User, default = 1, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return '%s %d %d %d %s' % (self.title, self.time_days, self.time_hours, self.time_minutes, self.description)

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'time_days','time_hours', 'time_minutes', 'description']
