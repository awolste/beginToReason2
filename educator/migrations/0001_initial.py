# Generated by Django 3.1.2 on 2021-03-31 17:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Class')),
                ('class_instructor', models.ManyToManyField(blank=True, related_name='Instructor', to='accounts.UserInformation')),
                ('lesson_plan', models.ManyToManyField(blank=True, to='core.MainSet')),
                ('student', models.ManyToManyField(blank=True, related_name='Student', to='accounts.UserInformation')),
            ],
        ),
    ]
