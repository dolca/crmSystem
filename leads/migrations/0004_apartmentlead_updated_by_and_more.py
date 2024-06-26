# Generated by Django 5.0.4 on 2024-05-29 10:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_alter_apartmentlead_floor_and_more'),
        ('listings', '0002_alter_apartment_floor_alter_commercialspace_floor_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentlead',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_apartment_leads', to=settings.AUTH_USER_MODEL, verbose_name='Actualizată de'),
        ),
        migrations.AddField(
            model_name='commercialspacelead',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_commercial_space_leads', to=settings.AUTH_USER_MODEL, verbose_name='Actualizată de'),
        ),
        migrations.AddField(
            model_name='houselead',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_house_leads', to=settings.AUTH_USER_MODEL, verbose_name='Actualizată de'),
        ),
        migrations.AddField(
            model_name='industrialspacelead',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_industrial_space_leads', to=settings.AUTH_USER_MODEL, verbose_name='Actualizată de'),
        ),
        migrations.AddField(
            model_name='officespacelead',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_office_space_leads', to=settings.AUTH_USER_MODEL, verbose_name='Actualizată de'),
        ),
        migrations.AddField(
            model_name='terrainlead',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_terrain_leads', to=settings.AUTH_USER_MODEL, verbose_name='Actualizată de'),
        ),
        migrations.AlterField(
            model_name='apartmentlead',
            name='assigned_listings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.apartment', verbose_name='Proprietăți asociate'),
        ),
        migrations.AlterField(
            model_name='apartmentlead',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_apartment_leads', to=settings.AUTH_USER_MODEL, verbose_name='Agent asociat'),
        ),
        migrations.AlterField(
            model_name='commercialspacelead',
            name='assigned_listings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.commercialspace', verbose_name='Proprietăți asociate'),
        ),
        migrations.AlterField(
            model_name='commercialspacelead',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_commercial_space_leads', to=settings.AUTH_USER_MODEL, verbose_name='Agent asociat'),
        ),
        migrations.AlterField(
            model_name='houselead',
            name='assigned_listings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.house', verbose_name='Proprietăți asociate'),
        ),
        migrations.AlterField(
            model_name='houselead',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_house_leads', to=settings.AUTH_USER_MODEL, verbose_name='Agent asociat'),
        ),
        migrations.AlterField(
            model_name='industrialspacelead',
            name='assigned_listings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.industrialspace', verbose_name='Proprietăți asociate'),
        ),
        migrations.AlterField(
            model_name='industrialspacelead',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_industrial_space_leads', to=settings.AUTH_USER_MODEL, verbose_name='Agent asociat'),
        ),
        migrations.AlterField(
            model_name='officespacelead',
            name='assigned_listings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.officespace', verbose_name='Proprietăți asociate'),
        ),
        migrations.AlterField(
            model_name='officespacelead',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_office_space_leads', to=settings.AUTH_USER_MODEL, verbose_name='Agent asociat'),
        ),
        migrations.AlterField(
            model_name='terrainlead',
            name='assigned_listings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.terrain', verbose_name='Proprietăți asociate'),
        ),
        migrations.AlterField(
            model_name='terrainlead',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_terrain_leads', to=settings.AUTH_USER_MODEL, verbose_name='Agent asociat'),
        ),
    ]
