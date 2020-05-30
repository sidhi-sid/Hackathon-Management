from django.shortcuts import render
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth
from django.contrib import auth

def home(request):
    return render(request, 'Hackathon/home.html' )

def signup(request):
    return render(request, 'Hackathon/signup.html' )

def login(request):
    return render(request, 'Hackathon/login.html' )


def login1(request):
    return render(request, 'Hackathon/login1.html' )


# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.get(email=request.POST['email'])
#                 return render(request, 'clg/signup.html', {'error': 'Email Id has already been taken'})
#             except User.DoesNotExist :
#                 user = User.objects.create_user(username =request.POST['username'], password =request.POST['password1'], email=request.POST['email'])
#                 auth.login(request, user)
#                 return render(request, 'clg/home.html')
#         else:
#             return render(request, 'clg/signup.html', {'error': 'password not matching'})
#     else:
#         return render(request, 'clg/signup.html')

# def login(request):
#     if request.method == 'POST':
#         user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
#         if user is not None:
#             auth.login(request, user)
#             return render(request, 'clg/book.html')
#         else:
#             return render(request, 'clg/login.html', {'error':'user not found..!!'})
#     else:
#         return render(request, 'clg/login.html')

def logout(request):
    # if request.method == 'POST':
    #     auth.logout(request)
        return render(request, 'clg/home.html')

def book(request):
    return render(request, 'clg/book.html')
