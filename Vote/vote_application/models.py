from django.db import models


class CreatePoll(models.Model):
    user_gmail = models.CharField(max_length=50, default='')
    id = models.AutoField(primary_key=True)
    que = models.CharField(max_length=30)
    polls = models.CharField(max_length=200)
    values = models.CharField(max_length=500, default='')
    total_vote = models.IntegerField(max_length=10000000, default=0)

    def __str__(self):
        return str(self.id)


class count_vote_user(models.Model):
    just_id = models.CharField(max_length=100000)
    email = models.CharField(max_length=50)

    def __str__(self):
        return str(self.just_id)
