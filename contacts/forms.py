from django.forms import ModelForm, TextInput, NumberInput, Textarea, Select, EmailInput, DateInput, SelectMultiple, \
    ClearableFileInput
from .models import Contact


class ContactUpdateForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'phone_number': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),

            'company': TextInput(attrs={'class': 'form-control'}),
            'job_title': TextInput(attrs={'class': 'form-control'}),

            'city': TextInput(attrs={'class': 'form-control'}),
            'street_address': TextInput(attrs={'class': 'form-control'}),
            'street_number': NumberInput(attrs={'class': 'form-control'}),
            'block': TextInput(attrs={'class': 'form-control'}),
            'scale': TextInput(attrs={'class': 'form-control'}),
            'apartment_number': NumberInput(attrs={'class': 'form-control'}),
            'county': TextInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control'}),

            'document_type': Select(attrs={'class': 'form-control'}),
            'id_series_nr': TextInput(attrs={'class': 'form-control'}),
            'cnp': TextInput(attrs={'class': 'form-control'}),
            'issue_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'passport_country': TextInput(attrs={'class': 'form-control'}),

            'contact_type': SelectMultiple(attrs={'class': 'form-control'}),
            'contact_category': SelectMultiple(attrs={'class': 'form-control'}),

            'avatar': ClearableFileInput(attrs={'class': 'form-control'}),
            'other_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'created_at': DateInput(attrs={'readonly': 'readonly'}),
            'updated_at': DateInput(attrs={'readonly': 'readonly'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        phone_number = cleaned_data.get('phone_number')
        email = cleaned_data.get('email')
        document_type = cleaned_data.get('document_type')
        id_series_nr = cleaned_data.get('id_series_nr')
        cnp = cleaned_data.get('cnp')
        issue_date = cleaned_data.get('issue_date')
        passport_country = cleaned_data.get('passport_country')

        if not first_name:
            self.add_error('first_name', 'Trebuie să introduci obligatoriu un prenume.')

        if not phone_number and not email:
            self.add_error('phone_number',
                           'Trebuie să introduci obligatoriu cel puțin un număr de telefon sau o adresă de e-mail.')

        if phone_number:
            self.validate_duplicate_field('phone_number', phone_number, contact_id=self.instance.id)

        if email:
            self.validate_duplicate_field('email', email, contact_id=self.instance.id)

        if document_type == 'Carte de identitate':
            if not id_series_nr:
                self.add_error('id_series_nr', 'Seria și numărul cărții de identitate sunt obligatorii.')
            if not id_series_nr.isupper() or not (len(id_series_nr) == 8 or len(id_series_nr) == 9):
                self.add_error('id_series_nr', 'Seria și numărul cărții de identitate sunt invalide. '
                                               '(ex. corect: "AZ 123456", cu majuscule)')

            if cnp and len(cnp) != 13:
                self.add_error('cnp', 'CNP-ul este invalid. Acesta trebuie să conțină exact 13 cifre.')

            if not issue_date:
                self.add_error('issue_date', 'Data emiterii cărții de identitate este obligatorie.')

        if document_type == 'Pașaport':
            if not id_series_nr:
                self.add_error('id_series_nr', 'Numărul pașaportului este obligatoriu.')
            if not id_series_nr.isupper() or not (len(id_series_nr) == 8 or len(id_series_nr) == 9):
                self.add_error('id_series_nr', 'Numărul pașaportului este invalid. '
                                               '(ex. corect, după caz: "123456789" sau "AZ1234567", cu majuscule)')

            if not issue_date:
                self.add_error('issue_date', 'Data emiterii pașaportului este obligatorie.')

            if not passport_country:
                self.add_error('passport_country', 'Țara emitentă a pașaportului este obligatorie.')

        return cleaned_data

    def validate_duplicate_field(self, field_name, value, contact_id=None):
        check_field = Contact.objects.exclude(id=contact_id).filter(**{field_name: value})

        if check_field.exists():
            if field_name == 'phone_number':
                msg = f'''Există deja un contact cu acest număr de telefon. 
                Introdu alt număr de telefon sau actualizează contactul existent.'''
                self.add_error(field_name, msg)
            elif field_name == 'email':
                msg = f'''Există deja un contact cu această adresă de e-mail. 
                Introdu altă adresă de e-mail sau actualizează contactul existent.'''
                self.add_error(field_name, msg)
