# Generated by Django 5.0.1 on 2024-01-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_application', '0007_createpoll_user_gmail'),
    ]

    operations = [
        migrations.CreateModel(
            name='count_vote_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('just_id', models.CharField(max_length=100000)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
