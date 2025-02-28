# Generated by Django 5.1.6 on 2025-02-17 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0014_examsubject_invigilator_checkin'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeatingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_app.studentprofile')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_app.examsubject')),
            ],
        ),
    ]
