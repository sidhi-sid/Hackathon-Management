# from django.contrib.auth.models import User, auth
from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from hackinfo2.models import Organiser, Userdata


def home(request):
    return render(request, 'Hackathon/home.html' )

def signup(request):
    return render(request, 'Hackathon/signup.html' )

# def login(request):
#     return render(request, 'Hackathon/login.html' )

def login(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            # if request.POST['code']  == 'L':
                prod = Userdata()
                prod.username = request.POST['username']
                prod.password = request.POST['password']
                prod.save()
                return render(request, 'hackinfo2/register.html')
            # else:
                # return render(request, 'Hackathon/login1.html', {'error' : 'code is incorrect'})
        else:
            return render(request, 'Hackathon/login.html', {'error' : 'All fields are required'})
    else:
        return render(request, 'Hackathon/login.html')

def login1(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            if request.POST['code']  == 'L':
                prod = Organiser()
                prod.username = request.POST['username']
                prod.password = request.POST['password']
                prod.save()
                return render(request, 'hackinfo2/organiserdashboard.html')
            else:
                return render(request, 'Hackathon/login1.html', {'error' : 'code is incorrect'})
        else:
            return render(request, 'Hackathon/login1.html', {'error' : 'All fields are required'})
    else:
        return render(request, 'Hackathon/login1.html')


def logout(request):
    # if request.method == 'POST':
    #     auth.logout(request)
        return render(request, 'clg/home.html')

def book(request):
    return render(request, 'clg/book.html')
