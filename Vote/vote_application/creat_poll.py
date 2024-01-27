from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CreatePoll, count_vote_user
from django.contrib import messages


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
        default_values = ','.join(['0'] * len(options))

        new_poll = CreatePoll(que=question, polls=', '.join(options), values=default_values, total_vote=0,
                              user_gmail=request.user.email)
        new_poll.save()
        return redirect('create_poll')


from django.shortcuts import get_object_or_404, redirect
from .models import CreatePoll, count_vote_user


def count_vote(request):
    if request.method == 'POST':
        poll_id = request.POST.get('poll_id')
        option_name = request.POST.get(f'poll_{poll_id}')
        user_email = request.user.email

        try:
            poll_data = get_object_or_404(CreatePoll, id=poll_id)
            poll_options = poll_data.polls
            total_poll = poll_data.total_vote
            polls_value = poll_data.values

            # Check if the user has already voted
            chake_identify = get_object_or_404(count_vote_user, just_id=poll_id, email=user_email)
            if chake_identify:
                error = "You already vote this poll"
                polls = CreatePoll.objects.all()

                username = request.user.username
                button_dispalay = 'd-none'
                user_display = 'd-flex'
                return render(request, 'vote_application/results.html',
                              {'username': username, 'button_dispalay': button_dispalay, 'user_display': user_display,
                               'polls': polls, 'error': error})




        except:

            # Assuming polls_value is a string like "1,2,3" and option_name is the option to be incremented
            polls_value_list = list(map(int, polls_value.strip('[]').split(',')))# Convert values to integers
            poll_options = list(map(str, poll_options.split(',')))  # Create a list of poll options

            cleaned_list = [item.strip() for item in poll_options]

            index = cleaned_list.index(option_name)
            polls_value_list[index] = polls_value_list[index] + 1
            total_poll = 0
            for i in range(len(polls_value_list)):
                total_poll += polls_value_list[i]

            poll_to_update = CreatePoll.objects.get(pk=poll_id)

            poll_to_update.values = polls_value_list
            poll_to_update.total_vote = total_poll
            poll_to_update.save()
            count_vote_user.objects.create(just_id=poll_id, email=user_email)

    return redirect('results')
