from django.shortcuts import render, redirect


def sign_up(request):
    return render(request, 'vote_application/Sign_up_.html')


def sign_up_data_collect(request):
    if request.method == 'POST':
        return redirect('login')
