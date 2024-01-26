from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CreatePoll


@login_required(login_url='login')
def creat_poll(request):
    username = request.user.username
    button_dispalay = 'd-none'
    user_display = 'd-flex'
    return render(request, 'vote_application/creat_poll.html',
                  {'username': username, 'button_dispalay': button_dispalay, 'user_display': user_display})


def save_data(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        options = request.POST.getlist('options[]')

        new_poll = CreatePoll(que=question, polls=', '.join(options))
        new_poll.save()
        return redirect('create_poll')
