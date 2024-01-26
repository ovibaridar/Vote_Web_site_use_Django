from django.db import models


# Create your models here.

class sign_up(models.Model):
    name = models.CharField(max_length=30)
    gmail = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.gmail
