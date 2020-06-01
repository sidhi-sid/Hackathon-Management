# from django.contrib.auth.models import User, auth
from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from hackinfo2.models import LeaderDetail

from django.contrib import auth

def homepage(request):
    return render(request, 'hackinfo2/homepage.html' )

def register(request):
    return render(request, 'hackinfo2/register.html' )

def tracker(request):
    return render(request, 'hackinfo2/tracker.html' )

def travel(request):
    return render(request, 'hackinfo2/travel.html' )

def project(request):
    return render(request, 'hackinfo2/project.html' )


# def register(request):
#     if request.method == 'POST':
#         if request.POST['teamname1'] and request.POST['firstname1'] and request.POST['lastname1'] and request.POST['gender1'] and request.POST['email1'] and request.POST['contact1'] and request.POST['college1'] and request.POST['yearofstudy1'] and request.POST['branch1'] and request.POST['github1'] and request.POST['linkedin1'] :
#                 prod = LeaderDetail()
#                 prod.teamname1 = request.POST['teamname1']
#                 prod.firstname1 = request.POST['firstname1']
#                 prod.lastname1 = request.POST['lastname1']
#                 prod.gender1 = request.POST['gender1']
#                 prod.email1 = request.POST['email1']
#                 prod.contact1 = request.POST['contact1']
#                 prod.college1 = request.POST['college1']
#                 prod.yearofstudy1 = request.POST['yearofstudy1']
#                 prod.branch1 = request.POST['branch1']
#                 prod.github1 = request.POST['github1']
#                 prod.linkedin1 = request.POST['linkedin1']
#                 prod.save()
#                 return render(request, 'hackinfo2/register1.html')
#
#         else:
#             return render(request, 'hackinfo2/register.html', {'error' : 'All fields are required'})
#     else:
#         return render(request, 'hackinfo2/register.html')

def register1(request):
    return render(request, 'hackinfo2/register1.html' )

def track(request):
    return render(request, 'hackinfo2/track.html' )

def logout(request):
    return render(request, 'Hackathon/home.html' )

def userdashboard(request):
    return render(request, 'hackinfo2/userdashboard.html' )

def organiserdashboard(request):
    return render(request, 'hackinfo2/organiserdashboard.html' )
