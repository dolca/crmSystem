from django.contrib.auth.models import User
from django.db.models import Model, CharField, IntegerField, TextField, EmailField, DateField, ForeignKey, \
    DateTimeField, ImageField, SET_NULL
from contacts.selectors import TIP_DOCUMENT, TIP_CONTACT, CATEGORIE_CONTACT


class Contact(Model):
    first_name = CharField(max_length=30, verbose_name='Prenume')
    last_name = CharField(max_length=30, null=True, blank=True, verbose_name='Nume de familie')
    phone_number = CharField(max_length=14, unique=True, null=True, blank=True, verbose_name='Număr de telefon')
    email = EmailField(max_length=50, unique=True, null=True, blank=True, verbose_name='Adresă de e-mail')

    company = CharField(max_length=50, blank=True, null=True, verbose_name='Companie')
    job_title = CharField(max_length=50, blank=True, null=True, verbose_name='Funcție')

    city = CharField(max_length=30, null=True, blank=True, verbose_name='Localitate')
    street_address = CharField(max_length=40, null=True, blank=True, verbose_name='Stradă')
    street_number = IntegerField(null=True, blank=True, verbose_name='Număr stradă')
    block = CharField(max_length=4, null=True, blank=True, verbose_name='Bloc')
    scale = CharField(max_length=3, null=True, blank=True, verbose_name='Scară')
    apartment_number = IntegerField(null=True, blank=True, verbose_name='Număr apartament')
    county = CharField(max_length=20, null=True, blank=True, verbose_name='Județ')
    country = CharField(max_length=50, null=True, blank=True, verbose_name='Țară')

    document_type = CharField(choices=TIP_DOCUMENT, null=True, blank=True, verbose_name='Tip document')
    id_series_nr = CharField(max_length=20, blank=True, null=True, verbose_name='Serie / Număr')
    cnp = CharField(max_length=13, null=True, blank=True, verbose_name='CNP')
    issue_date = DateField(null=True, blank=True, verbose_name='Data emiterii')
    passport_country = CharField(max_length=50, blank=True, null=True, verbose_name='Țara emitentă (doar pentru pașaport)')

    contact_type = CharField(choices=TIP_CONTACT, null=True, blank=True, verbose_name='Tip contact')
    contact_category = CharField(choices=CATEGORIE_CONTACT, null=True, blank=True, verbose_name='Categorie')

    other_details = TextField(max_length=2000, null=True, blank=True, verbose_name='Alte detalii')

    avatar = ImageField(upload_to='media/contact_avatars', null=True, blank=True, verbose_name='Avatar')

    created_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='created_contact',
                            verbose_name='Adăugat de')
    updated_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='updated_contact',
                            verbose_name='Actualizat de')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Adăugat în')
    updated_at = DateTimeField(auto_now=True, verbose_name='Actualizat în')

    def save(self, *args, **kwargs):
        if self.first_name:
            self.first_name = self.first_name.title()

        if self.last_name:
            self.last_name = self.last_name.title()

        if self.email:
            self.email = self.email.lower()

        if self.company:
            self.company = self.company.upper()

        if self.job_title:
            self.job_title = self.job_title.title()

        if self.city:
            self.city = self.city.title()

        if self.street_address:
            self.street_address = self.street_address.title()

        if self.county:
            self.county = self.county.title()

        if self.country:
            self.country = self.country.title()

        if self.id_series_nr:
            self.id_series_nr = self.id_series_nr.upper()

        if self.passport_country:
            self.passport_country = self.passport_country.title()

        if self.other_details:
            self.other_details = self.other_details.capitalize()

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
