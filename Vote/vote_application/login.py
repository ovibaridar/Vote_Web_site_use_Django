# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout



def login(request):
    if request.user.is_authenticated:
        username = request.user.username
        button_dispalay = 'd-none'
        user_display = 'd-flex'
        return redirect("Home")
    else:
        button_dispalay = 'd-flex'
        user_display = 'd-none'
        return render(request , 'vote_application/login.html', {'button_dispalay': button_dispalay, 'user_display': user_display})


def log_in_(request):
    if request.method == 'POST':
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        password = str(password)
        print(gmail, password)

        user = authenticate(request, email=gmail, password=password)

        if user is not None:
            print(user.username)
            auth_login(request, user)
            return redirect('Home')
        else:
            error = 'Your email or password is wrong'
            return render(request, 'vote_application/login.html', {'error': error})





