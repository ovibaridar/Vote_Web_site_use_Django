from django.shortcuts import render


def results(request):
    return render(request, 'vote_application/results.html')
