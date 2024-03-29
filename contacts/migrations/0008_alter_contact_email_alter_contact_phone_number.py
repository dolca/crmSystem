# Generated by Django 5.0.2 on 2024-03-08 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_alter_contact_email_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True, verbose_name='Adresă de e-mail'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='Număr de telefon'),
        ),
    ]
