# Generated by Django 5.0.1 on 2024-01-25 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sign_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Gmail', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]