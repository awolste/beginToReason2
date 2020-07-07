# Generated by Django 3.0.8 on 2020-07-07 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=30)),
                ('lesson_code', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='McChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_key', models.CharField(max_length=30)),
                ('reference_text', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Reasoning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reasoning_name', models.CharField(max_length=30)),
                ('reasoning_type', models.CharField(choices=[('MC', 'Multiple Choice'), ('Text', 'Free Response'), ('Both', 'Multiple Choice and Free Response')], default='MC', max_length=4)),
                ('mc_set', models.ManyToManyField(blank=True, to='core.McChoice')),
                ('reasoning_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Question')),
            ],
        ),
        migrations.AddField(
            model_name='mcchoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Question'),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=50)),
                ('lesson_concept', models.CharField(max_length=50)),
                ('instruction', models.TextField()),
                ('screen_record', models.BooleanField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Code')),
                ('reason', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Reasoning')),
                ('reference_set', models.ManyToManyField(blank=True, to='core.Reference')),
            ],
        ),
    ]
