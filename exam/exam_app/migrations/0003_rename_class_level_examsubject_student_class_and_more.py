# Generated by Django 5.0.1 on 2024-02-03 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_examroom_examsubject_delete_exam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examsubject',
            old_name='class_level',
            new_name='student_class',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='class_level',
            new_name='student_class',
        ),
    ]
