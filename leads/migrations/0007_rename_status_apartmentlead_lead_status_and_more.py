# Generated by Django 5.0.3 on 2024-04-01 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_remove_apartmentlead_deadline_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartmentlead',
            old_name='status',
            new_name='lead_status',
        ),
        migrations.RenameField(
            model_name='commercialspacelead',
            old_name='status',
            new_name='lead_status',
        ),
        migrations.RenameField(
            model_name='houselead',
            old_name='status',
            new_name='lead_status',
        ),
        migrations.RenameField(
            model_name='industrialspacelead',
            old_name='status',
            new_name='lead_status',
        ),
        migrations.RenameField(
            model_name='officespacelead',
            old_name='status',
            new_name='lead_status',
        ),
        migrations.RenameField(
            model_name='terrainlead',
            old_name='status',
            new_name='lead_status',
        ),
    ]
