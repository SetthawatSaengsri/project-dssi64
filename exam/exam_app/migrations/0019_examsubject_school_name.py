# Generated by Django 5.1.6 on 2025-03-30 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0018_examsubject_secondary_invigilator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='examsubject',
            name='school_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
