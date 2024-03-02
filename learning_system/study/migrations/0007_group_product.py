# Generated by Django 5.0.2 on 2024-02-29 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_productaccess_user'),
        ('study', '0006_remove_group_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.product'),
            preserve_default=False,
        ),
    ]
