from django.forms import ModelForm, TextInput, NumberInput, Textarea, Select, CheckboxSelectMultiple, EmailInput, \
    DateInput, ClearableFileInput
from .models import Contact
from django.core.exceptions import ValidationError


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

            'contact_type': Select(attrs={'class': 'form-control'}),
            'contact_category': Select(attrs={'class': 'form-control'}),

            'other_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'avatar': ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise ValidationError('Trebuie să introduci obligatoriu un prenume.')
        return first_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not (10 <= len(phone_number) <= 14):
            raise ValidationError('Numărul de telefon trebuie să conțină între 10 și 14 cifre.')
        if phone_number:
            self.validate_duplicate_field('phone_number', phone_number, contact_id=self.instance.id)
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            self.validate_duplicate_field('email', email, contact_id=self.instance.id)
        return email

    def clean_id_series_nr(self):
        document_type = self.cleaned_data.get('document_type')
        id_series_nr = self.cleaned_data.get('id_series_nr')
        if document_type == 'Carte de identitate':
            if not id_series_nr:
                raise ValidationError('Seria și numărul cărții de identitate sunt obligatorii.')
            if not id_series_nr.isupper() or not (len(id_series_nr) == 8 or len(id_series_nr) == 9):
                raise ValidationError('Seria și numărul cărții de identitate sunt invalide. '
                                      '(ex. corect: "AZ 123456", cu majuscule)')
        elif document_type == 'Pașaport':
            if not id_series_nr:
                raise ValidationError('Numărul pașaportului este obligatoriu.')
            if not id_series_nr.isupper() or not (len(id_series_nr) == 8 or len(id_series_nr) == 9):
                raise ValidationError('Numărul pașaportului este invalid. '
                                      '(ex. corect, după caz: "123456789" sau "AZ1234567", cu majuscule)')
        return id_series_nr

    def clean_cnp(self):
        document_type = self.cleaned_data.get('document_type')
        company = self.cleaned_data.get('company')
        job_title = self.cleaned_data.get('job_title')
        cnp = self.cleaned_data.get('cnp')
        if document_type == 'Carte de identitate' and cnp:
            if len(cnp) != 13:
                raise ValidationError('CNP-ul este invalid. Acesta trebuie să conțină exact 13 cifre.')
        elif document_type == 'Certificat de înregistrare' and cnp:
            if not cnp:
                raise ValidationError('CUI-ul companiei este obligatoriu.')
            if cnp.startswith('RO'):
                cnp_num = cnp[2:]
            else:
                cnp_num = cnp

            if not (7 <= len(cnp_num) <= 8 and cnp_num.isdigit()):
                raise ValidationError('CUI-ul este invalid. (ex. corect, după caz: "12345678" sau "RO12345678", '
                                      'cu majuscule.)')
            if not company:
                raise ValidationError('Numele companiei este obligatoriu.')
            if not job_title:
                raise ValidationError('Funcția în companie este obligatorie.')
        return cnp

    def clean_issue_date(self):
        document_type = self.cleaned_data.get('document_type')
        issue_date = self.cleaned_data.get('issue_date')
        if issue_date == 'undefined-undefined-':
            issue_date = None
        if document_type == 'Carte de identitate' and not issue_date:
            raise ValidationError('Data emiterii cărții de identitate este obligatorie.')
        elif document_type == 'Pașaport' and not issue_date:
            raise ValidationError('Data emiterii pașaportului este obligatorie.')
        return issue_date

    def clean_passport_country(self):
        document_type = self.cleaned_data.get('document_type')
        passport_country = self.cleaned_data.get('passport_country')
        if document_type == 'Pașaport' and not passport_country:
            raise ValidationError('Țara emitentă a pașaportului este obligatorie.')
        return passport_country

    def validate_duplicate_field(self, field_name, value, contact_id=None):
        check_field = Contact.objects.exclude(id=contact_id).filter(**{field_name: value})
        if check_field.exists():
            if field_name == 'phone_number':
                raise ValidationError('Există deja un contact cu acest număr de telefon. '
                                      'Introdu alt număr de telefon sau actualizează contactul existent.')
            elif field_name == 'email':
                raise ValidationError('Există deja un contact cu această adresă de e-mail. '
                                      'Introdu altă adresă de e-mail sau actualizează contactul existent.')

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number')
        email = cleaned_data.get('email')

        if not phone_number and not email:
            raise ValidationError('Trebuie să introduci obligatoriu cel puțin un '
                                  'număr de telefon sau o adresă de e-mail.')

        return cleaned_data
