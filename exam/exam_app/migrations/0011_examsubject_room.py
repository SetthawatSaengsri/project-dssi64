# Generated by Django 5.0.1 on 2025-01-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0010_examsubject'),
    ]

    operations = [
        migrations.AddField(
            model_name='examsubject',
            name='room',
            field=models.CharField(blank=True, max_length=20, verbose_name='ห้องสอบ'),
        ),
    ]
