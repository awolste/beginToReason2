# Generated by Django 3.1.1 on 2020-11-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201030_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonset',
            name='set_image',
            field=models.ImageField(default='begin.png', upload_to=None),
        ),
    ]
