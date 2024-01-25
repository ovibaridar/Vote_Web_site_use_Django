from django.shortcuts import render


def home(request):
    return render(request, 'vote_application/home.html')
