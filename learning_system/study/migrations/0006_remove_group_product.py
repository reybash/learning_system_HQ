# Generated by Django 5.0.2 on 2024-02-29 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_remove_group_products_group_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='product',
        ),
    ]
