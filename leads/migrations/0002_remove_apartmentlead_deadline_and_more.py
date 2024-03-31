# Generated by Django 5.0.3 on 2024-03-31 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentlead',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='commercialspacelead',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='houselead',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='industrialspacelead',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='officespacelead',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='terrainlead',
            name='deadline',
        ),
        migrations.AddField(
            model_name='apartmentlead',
            name='deadline_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data limită'),
        ),
        migrations.AddField(
            model_name='apartmentlead',
            name='deadline_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Ora limită'),
        ),
        migrations.AddField(
            model_name='commercialspacelead',
            name='deadline_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data limită'),
        ),
        migrations.AddField(
            model_name='commercialspacelead',
            name='deadline_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Ora limită'),
        ),
        migrations.AddField(
            model_name='houselead',
            name='deadline_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data limită'),
        ),
        migrations.AddField(
            model_name='houselead',
            name='deadline_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Ora limită'),
        ),
        migrations.AddField(
            model_name='industrialspacelead',
            name='deadline_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data limită'),
        ),
        migrations.AddField(
            model_name='industrialspacelead',
            name='deadline_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Ora limită'),
        ),
        migrations.AddField(
            model_name='officespacelead',
            name='deadline_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data limită'),
        ),
        migrations.AddField(
            model_name='officespacelead',
            name='deadline_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Ora limită'),
        ),
        migrations.AddField(
            model_name='terrainlead',
            name='deadline_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data limită'),
        ),
        migrations.AddField(
            model_name='terrainlead',
            name='deadline_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Ora limită'),
        ),
        migrations.AlterField(
            model_name='apartmentlead',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contact', verbose_name='Contact asociat⋆'),
        ),
        migrations.AlterField(
            model_name='apartmentlead',
            name='property_type',
            field=models.CharField(choices=[('apartment', 'Apartament'), ('house', 'Casă'), ('terrain', 'Teren'), ('commercial_space', 'Spațiu comercial'), ('office_space', 'Spațiu de birouri'), ('industrial_space', 'Spațiu industrial')], default='apartment', verbose_name='Tip cerere⋆'),
        ),
        migrations.AlterField(
            model_name='commercialspacelead',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contact', verbose_name='Contact asociat⋆'),
        ),
        migrations.AlterField(
            model_name='commercialspacelead',
            name='property_type',
            field=models.CharField(choices=[('apartment', 'Apartament'), ('house', 'Casă'), ('terrain', 'Teren'), ('commercial_space', 'Spațiu comercial'), ('office_space', 'Spațiu de birouri'), ('industrial_space', 'Spațiu industrial')], default='apartment', verbose_name='Tip cerere⋆'),
        ),
        migrations.AlterField(
            model_name='houselead',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contact', verbose_name='Contact asociat⋆'),
        ),
        migrations.AlterField(
            model_name='houselead',
            name='property_type',
            field=models.CharField(choices=[('apartment', 'Apartament'), ('house', 'Casă'), ('terrain', 'Teren'), ('commercial_space', 'Spațiu comercial'), ('office_space', 'Spațiu de birouri'), ('industrial_space', 'Spațiu industrial')], default='apartment', verbose_name='Tip cerere⋆'),
        ),
        migrations.AlterField(
            model_name='industrialspacelead',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contact', verbose_name='Contact asociat⋆'),
        ),
        migrations.AlterField(
            model_name='industrialspacelead',
            name='property_type',
            field=models.CharField(choices=[('apartment', 'Apartament'), ('house', 'Casă'), ('terrain', 'Teren'), ('commercial_space', 'Spațiu comercial'), ('office_space', 'Spațiu de birouri'), ('industrial_space', 'Spațiu industrial')], default='apartment', verbose_name='Tip cerere⋆'),
        ),
        migrations.AlterField(
            model_name='officespacelead',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contact', verbose_name='Contact asociat⋆'),
        ),
        migrations.AlterField(
            model_name='officespacelead',
            name='property_type',
            field=models.CharField(choices=[('apartment', 'Apartament'), ('house', 'Casă'), ('terrain', 'Teren'), ('commercial_space', 'Spațiu comercial'), ('office_space', 'Spațiu de birouri'), ('industrial_space', 'Spațiu industrial')], default='apartment', verbose_name='Tip cerere⋆'),
        ),
        migrations.AlterField(
            model_name='terrainlead',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contact', verbose_name='Contact asociat⋆'),
        ),
        migrations.AlterField(
            model_name='terrainlead',
            name='property_type',
            field=models.CharField(choices=[('apartment', 'Apartament'), ('house', 'Casă'), ('terrain', 'Teren'), ('commercial_space', 'Spațiu comercial'), ('office_space', 'Spațiu de birouri'), ('industrial_space', 'Spațiu industrial')], default='apartment', verbose_name='Tip cerere⋆'),
        ),
    ]
