from django.shortcuts import render
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth
from django.contrib import auth

def homepage(request):
    return render(request, 'hackinfo/homepage.html' )

def register(request):
    return render(request, 'hackinfo/register.html' )

def track(request):
    return render(request, 'hackinfo/track.html' )

def logout(request):
    return render(request, 'Hackathon/home.html' )
