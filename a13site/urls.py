"""a13site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login import views

from django.views.generic import TemplateView

app_name = 'a13site'

urlpatterns = [
    path('', TemplateView.as_view(template_name="login/index.html")),
    path('addexercise',views.exercise_view, name='exercise-view'),
    path('exercises',views.ExercisesView.as_view(),name='exercises'),
    path('addreminder',views.reminder_view, name='reminder-view'),
    path('reminders',views.RemindersView.as_view(),name='reminders'),
    path('profile', views.profile_view, name='profile'),
    path('leaderboard', views.leaderboard_view, name='leaderboard'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('calendar', views.event_view, name='calendar'),
    path('authorize/', views.authorize),
]
