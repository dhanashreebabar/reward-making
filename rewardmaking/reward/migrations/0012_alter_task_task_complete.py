# Generated by Django 4.1.7 on 2023-03-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0011_task_task_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_complete',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
