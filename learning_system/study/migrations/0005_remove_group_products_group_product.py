# Generated by Django 5.0.2 on 2024-02-29 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_productaccess_user'),
        ('study', '0004_remove_lesson_video_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='products',
        ),
        migrations.AddField(
            model_name='group',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='catalog.product'),
            preserve_default=False,
        ),
    ]
