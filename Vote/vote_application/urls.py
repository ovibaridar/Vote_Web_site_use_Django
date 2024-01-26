from django.contrib import admin
from django.urls import path
from . import views

from .import sign_up
from .import login
from .import creat_poll
from .import results
from .import logout


urlpatterns = [
    path('', views.home, name='Home'),
    path('sign_up', sign_up.sign_up, name='sign_up'),
    path('sign_up_data_collect', sign_up.sign_up_data_collect, name='sign_up_data_collect'),
    path('login', login.login, name='login'),
    path('log_in_', login.log_in_, name='log_in_'),
    path('logout/', logout.user_logout, name='logout'),
    path('create_poll', creat_poll.creat_poll, name='create_poll'),
    path('count_vote', creat_poll.count_vote, name='count_vote'),
    path('save_data', creat_poll.save_data, name='save_data'),
    path('results', results.results, name='results'),
]
