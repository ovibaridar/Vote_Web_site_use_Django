# views.py
from django.shortcuts import render, redirect
from .models import sign_up as SignUpModel  # Rename the model to avoid conflict
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def sign_up(request):
    if request.user.is_authenticated:
        username = request.user.username
        button_dispalay = 'd-none'
        user_display = 'd-flex'
        return redirect("Home")
    else:
        button_dispalay = 'd-flex'
        user_display = 'd-none'
        return render(request, 'vote_application/Sign_up_.html',
                      {'button_dispalay': button_dispalay, 'user_display': user_display})


def sign_up_data_collect(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        gmail = request.POST.get('email')
        password = request.POST.get('password')
        # You may want to add validation and error handling here
        if User.objects.filter(email=gmail).exists():
            error = "This email is already in use."
            return render(request, 'vote_application/Sign_up_.html', {'error': error})
        # Save the data to the database using the renamed model
        else:
            my_user = User.objects.create_user(name, gmail, password)
            my_user.save()
            return redirect('login')

    return render(request, 'vote_application/Sign_up_.html')
