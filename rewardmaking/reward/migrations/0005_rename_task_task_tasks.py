# Generated by Django 4.1.7 on 2023-03-27 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0004_tasklinks_alter_task_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='tasks',
        ),
    ]