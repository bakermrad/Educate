# Generated by Django 4.2 on 2023-04-09 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_end_time_alter_course_start_time'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('name', 'day', 'start_time', 'end_time')},
        ),
    ]
