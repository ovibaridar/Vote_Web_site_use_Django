from django.contrib import admin

# Register your models here.
from .models import CreatePoll ,count_vote_user

admin.site.register(CreatePoll)
admin.site.register(count_vote_user)
