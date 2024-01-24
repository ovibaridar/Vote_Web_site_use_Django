"""
URL configuration for Vote project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from . import sign_up
from . import login
from . import creat_poll
from . import results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('sign_up', sign_up.sign_up, name='sign_up'),
    path('login', login.login, name='login'),
    path('create_poll', creat_poll.creat_poll, name='create_poll'),
    path('results', results.results, name='results'),
]
