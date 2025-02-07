# Generated by Django 5.0.1 on 2025-01-07 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0003_alter_user_options_user_unique_username_per_school'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='user',
            name='unique_username_per_school',
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('username', 'school_name')},
        ),
    ]
