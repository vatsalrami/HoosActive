from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import ExerciseForm, Exercise, Reminder, ReminderForm
from django.views import generic
from django.contrib import auth
from datetime import datetime, timedelta
from django.db.models import Sum
import datefinder
from django.conf import settings
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import requests

from twilio.rest import Client


import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/userinfo.profile','https://www.googleapis.com/auth/userinfo.email','https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events']
# Create your views here.


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'credentials.json')

CLIENT_SECRETS_FILE = my_file


REDIRECT_URI = "http://a13site.herokuapp.com/calendar"

state = ''

flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE,SCOPES)

def authorize(request):
    flow.redirect_uri = REDIRECT_URI
    
    authorization_url, state = flow.authorization_url(access_type='online',
    include_granted_scopes = 'true', approval_prompt = 'force')
    
    return HttpResponseRedirect(authorization_url)

def event_view(request):
    context = {}

    exercises_obj = Exercise.objects.all()

    code = ''
    
    if request.method == 'POST':
        # start = request.POST['datetimeText']
        # summary = request.POST['titleText']
        # duration = request.POST['durationNum']
        # evt_desc = request.POST['descText']
        phone_num =request.POST['phone']
        hidden_desc = request.POST['descHidd']
        send_msg(phone_num,hidden_desc)
        # location = request.POST['placeText']
        # code = request.GET['code']
        # resp = create_event(start,summary,duration,code, evt_desc,location)
        return HttpResponseRedirect("calendar")
 
        #TODO: call create_event and send exercises fields

    # context['form'] = form
    context['exercises_obj'] = exercises_obj
    return render(request, "login/calendar.html", context)

def send_msg(num, message):
    account_sid = 'ACdc160c24dce730cfd66a40e8d6b24cea'
    auth_token = '81355f3d9ac00049114de53987f10b69'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body=message,
            from_='+16145917980',
            to=num
            )
            
def create_event(start_time_str,summary,duration, code,description=None,location=None):
    creds = None

    auth_code = code

    flow.fetch_token(code=auth_code)
    creds = flow.credentials

    # if os.path.exists('token.json'): check locally if user info has already been authenticated
    #     creds = Credentials.from_authorized_user_file('token.json',SCOPES)
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(os.path.join(settings.BASE_DIR, 'login\\static\\login\\credentials.json'),SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     with open('token.json','w') as token:
    #         token.write(creds.to_json())
    service = build('calendar','v3',credentials=creds)

    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(minutes=int(duration))

        event = {
            'summary':summary,
            'location': location,
            'description': description,
            'start':{
                'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': 'US/Eastern',
            },
            'end':{
                'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': 'US/Eastern',
            },
            'reminders':{
                'useDefault': False,
                'overrides':[
                    {'method':'email','minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        result = service.events().insert(calendarId='primary',body=event).execute()


class ExercisesView(generic.ListView):
    model = Exercise
    template_name = 'login/exercise_list.html'
    context_object_name = "exercise_list"


def exercise_view(request):
    context = {}

    form = ExerciseForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user
        obj.points = int(obj.rpe[:1]) * obj.time
        obj.save()
        form = ExerciseForm()

    context['form'] = form
    return render(request, "login/exercise.html",context)  
    
def profile_view(request):
    total_points = Exercise.objects.filter(user=request.user).aggregate(Sum('points'))
    rankings = {}
    all_exercises = Exercise.objects.all()
    for exercise in all_exercises:
        if (rankings.get(exercise.user, 0) == 0):
            rankings[exercise.user] = exercise.points
        else:
            rankings[exercise.user] += exercise.points    
    
        sorted_rankings = sorted(rankings.items(), key = lambda kv: kv[1])
        sorted_rankings.reverse()
    try:
        rank = [x[0] for x in sorted_rankings].index(request.user) + 1
    except ValueError:
        rank = "N/A"
        
    context = {
    'exercise_list': Exercise.objects.all(), 
    'total_points':total_points,
    'rank': rank,
    }
    return render(request, 'login/profile_exercise_list.html', context)

def leaderboard_view(request):
    rankings = {}
    all_exercises = Exercise.objects.all()
    for exercise in all_exercises:
        if (rankings.get(exercise.user, 0) == 0):
            rankings[exercise.user] = exercise.points
        else:
            rankings[exercise.user] += exercise.points    
    
    sorted_rankings = sorted(rankings.items(), key = lambda kv: kv[1])
    sorted_rankings.reverse()    
        
    context = {
    'sorted_rankings': sorted_rankings,
    }
    return render(request, 'login/leaderboard.html', context)    


class RemindersView(generic.ListView):
    model = Reminder
    template_name = 'login/reminder_list.html'
    context_object_name = "reminder_list"

def reminder_view(request):
    context = {}

    form = ReminderForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user
        form.save()
        form = ReminderForm()
    
    context['form'] = form
    return render(request, "login/reminder.html",context)

