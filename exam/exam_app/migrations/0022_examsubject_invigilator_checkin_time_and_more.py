# Generated by Django 5.1.6 on 2025-04-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0021_examsubject_qr_expiration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='examsubject',
            name='invigilator_checkin_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examsubject',
            name='secondary_invigilator_checkin_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
