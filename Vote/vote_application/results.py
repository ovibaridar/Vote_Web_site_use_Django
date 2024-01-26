from django.shortcuts import render


def results(request):
    if request.user.is_authenticated:
        username = request.user.username
        button_dispalay = 'd-none'
        user_display = 'd-flex'
        return render(request, 'vote_application/results.html',
                      {'username': username, 'button_dispalay': button_dispalay, 'user_display': user_display})
    else:
        button_dispalay = 'd-flex'
        user_display = 'd-none'
        return render(request, 'vote_application/results.html',
                      {'button_dispalay': button_dispalay, 'user_display': user_display})

