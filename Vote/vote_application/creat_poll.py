from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def creat_poll(request):
    username = request.user.username
    button_dispalay = 'd-none'
    user_display = 'd-flex'
    return render(request, 'vote_application/creat_poll.html',
                  {'username': username, 'button_dispalay': button_dispalay, 'user_display': user_display})
