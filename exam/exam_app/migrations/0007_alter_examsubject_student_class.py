# Generated by Django 5.0.1 on 2024-02-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0006_alter_examroom_capacity_alter_user_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examsubject',
            name='student_class',
            field=models.CharField(choices=[('1/1', '1/1'), ('1/2', '1/2'), ('2/1', '2/1'), ('2/2', '2/2'), ('3/1', '3/1'), ('3/2', '3/2'), ('4/1', '4/1'), ('4/2', '4/2'), ('5/1', '5/1'), ('5/2', '5/2'), ('6/1', '6/1'), ('6/2', '6/2')], max_length=10),
        ),
    ]
