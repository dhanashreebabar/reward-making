# Generated by Django 4.1.7 on 2023-03-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
