# Generated by Django 5.0.3 on 2024-04-01 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_apartment_property_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='status',
            new_name='property_status',
        ),
        migrations.RenameField(
            model_name='commercialspace',
            old_name='status',
            new_name='property_status',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='status',
            new_name='property_status',
        ),
        migrations.RenameField(
            model_name='industrialspace',
            old_name='status',
            new_name='property_status',
        ),
        migrations.RenameField(
            model_name='officespace',
            old_name='status',
            new_name='property_status',
        ),
        migrations.RenameField(
            model_name='terrain',
            old_name='status',
            new_name='property_status',
        ),
    ]
