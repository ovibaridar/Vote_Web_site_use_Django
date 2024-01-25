from django.contrib import admin
from django.urls import path
from . import views

from .import sign_up
from .import login
from .import creat_poll
from .import results


urlpatterns = [
    path('', views.home, name='Home'),
    path('sign_up', sign_up.sign_up, name='sign_up'),
    path('sign_up_data_collect', sign_up.sign_up_data_collect, name='sign_up_data_collect'),
    path('login', login.login, name='login'),
    path('create_poll', creat_poll.creat_poll, name='create_poll'),
    path('results', results.results, name='results'),
]
