# Generated by Django 3.2 on 2023-03-19 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20230319_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owned_flats',
            new_name='flats',
        ),
    ]
