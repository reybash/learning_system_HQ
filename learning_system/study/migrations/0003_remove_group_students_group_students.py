# Generated by Django 5.0.2 on 2024-02-29 11:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_remove_group_students_alter_lesson_product_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='students',
        ),
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
