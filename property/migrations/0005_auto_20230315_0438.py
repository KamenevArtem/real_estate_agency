# Generated by Django 2.2.24 on 2023-03-15 01:38

from django.db import migrations

def fill_Flat_new_building_field(property, schema_editor):
    Flat = property.get_model('property', 'Flat')
    flats = Flat.objects.values(
        'construction_year'
        ).filter(
            construction_year__gte=2015
            ).update(
                new_building=True
                )
    flats = Flat.objects.values(
        'construction_year'
        ).filter(
            construction_year__lt=2015
            ).update(
                new_building=False
                )



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20230315_0326'),
    ]

    operations = [
        migrations.RunPython(fill_Flat_new_building_field)
    ]

