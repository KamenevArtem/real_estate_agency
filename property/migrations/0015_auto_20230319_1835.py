# Generated by Django 3.2 on 2023-03-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20230318_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(blank=True, db_index=True, null=True, verbose_name='Является новостройкой?'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owned_flats',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
