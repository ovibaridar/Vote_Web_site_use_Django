
from django.shortcuts import render


def creat_poll(request):
    return render(request, 'vote_application/creat_poll.html')



