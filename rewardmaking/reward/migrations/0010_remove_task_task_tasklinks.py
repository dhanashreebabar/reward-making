# Generated by Django 4.1.7 on 2023-03-27 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reward', '0009_alter_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task',
        ),
        migrations.CreateModel(
            name='TaskLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtubelink', models.URLField(max_length=2000)),
                ('video', models.URLField(max_length=2000)),
                ('ig', models.URLField(max_length=2000)),
                ('share', models.URLField(max_length=2000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
