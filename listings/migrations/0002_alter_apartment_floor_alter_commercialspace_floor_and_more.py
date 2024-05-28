# Generated by Django 5.0.4 on 2024-05-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='floor',
            field=models.CharField(choices=[('Demisol', 'Demisol'), ('Parter', 'Parter'), ('Parter înalt', 'Parter înalt'), ('Etaj intermediar', 'Etaj intermediar'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('Mansardă', 'Mansardă'), ('Ultimele 2 etaje', 'Ultimele 2 etaje')], verbose_name='Etaj'),
        ),
        migrations.AlterField(
            model_name='commercialspace',
            name='floor',
            field=models.CharField(choices=[('Demisol', 'Demisol'), ('Parter', 'Parter'), ('Parter înalt', 'Parter înalt'), ('Mezanin', 'Mezanin'), ('Etaj intermediar', 'Etaj intermediar'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('Mansardă', 'Mansardă'), ('Ultimele 2 etaje', 'Ultimele 2 etaje')], verbose_name='Etaj'),
        ),
        migrations.AlterField(
            model_name='officespace',
            name='floor',
            field=models.CharField(choices=[('Demisol', 'Demisol'), ('Parter', 'Parter'), ('Parter înalt', 'Parter înalt'), ('Mezanin', 'Mezanin'), ('Etaj intermediar', 'Etaj intermediar'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('Mansardă', 'Mansardă'), ('Ultimele 2 etaje', 'Ultimele 2 etaje')], verbose_name='Etaj'),
        ),
    ]
