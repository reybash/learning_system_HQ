# Generated by Django 5.0.2 on 2024-03-02 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_productaccess_is_valid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_available',
        ),
    ]
