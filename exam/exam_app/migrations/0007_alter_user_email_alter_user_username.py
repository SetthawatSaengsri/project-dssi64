# Generated by Django 5.0.1 on 2025-01-09 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0006_alter_studentprofile_student_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]
