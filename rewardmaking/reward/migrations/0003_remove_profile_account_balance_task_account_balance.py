# Generated by Django 4.1.7 on 2023-03-27 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0002_alter_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='account_balance',
        ),
        migrations.AddField(
            model_name='task',
            name='account_balance',
            field=models.FloatField(default=100),
        ),
    ]