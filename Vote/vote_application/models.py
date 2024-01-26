from django.db import models


class CreatePoll(models.Model):
    id = models.AutoField(primary_key=True)
    que = models.CharField(max_length=30)
    polls = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)
