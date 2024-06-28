# Generated by Django 5.1b1 on 2024-06-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_avatar_contact_created_by_contact_updated_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cnp',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='CNP / CUI'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='document_type',
            field=models.CharField(blank=True, choices=[('Carte de identitate', 'Carte de identitate'), ('Pașaport', 'Pașaport'), ('Certificat de înregistrare', 'Certificat de înregistrare'), ('Alt document', 'Alt document')], null=True, verbose_name='Tip document'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id_series_nr',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Serie / Număr / J'),
        ),
    ]
