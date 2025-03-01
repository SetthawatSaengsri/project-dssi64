# Generated by Django 5.0.1 on 2025-01-09 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0007_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='exam_subject',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='student',
        ),
        migrations.RemoveField(
            model_name='examsubject',
            name='exam_room',
        ),
        migrations.RemoveField(
            model_name='examsubject',
            name='attendance',
        ),
        migrations.RemoveField(
            model_name='examsubject',
            name='invigilator',
        ),
        migrations.RemoveField(
            model_name='examsubject',
            name='student_class',
        ),
        migrations.RemoveField(
            model_name='examsubject',
            name='students',
        ),
        migrations.RemoveField(
            model_name='examsubject',
            name='subject_teacher',
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='student_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AddConstraint(
            model_name='studentprofile',
            constraint=models.UniqueConstraint(fields=('student_id', 'user'), name='unique_student_per_user'),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='ExamRoom',
        ),
        migrations.DeleteModel(
            name='ExamSubject',
        ),
    ]
