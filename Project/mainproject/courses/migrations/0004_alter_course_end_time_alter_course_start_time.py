# Generated by Django 4.2 on 2023-04-09 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_course_time_course_end_time_course_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
