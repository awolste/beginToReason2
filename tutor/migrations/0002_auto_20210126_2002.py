# Generated by Django 3.1.2 on 2021-01-27 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonlog',
            old_name='user_key',
            new_name='user',
        ),
    ]
