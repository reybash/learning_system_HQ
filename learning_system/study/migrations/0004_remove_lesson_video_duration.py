# Generated by Django 5.0.2 on 2024-02-29 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_remove_group_students_group_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='video_duration',
        ),
    ]
