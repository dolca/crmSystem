# Generated by Django 5.0.4 on 2024-06-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_apartmentlead_custom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentlead',
            name='custom_id',
            field=models.CharField(editable=False, max_length=15, unique=True, verbose_name='ID'),
        ),
    ]