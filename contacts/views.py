from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, TemplateView
from contacts.models import Contact
from contacts.forms import ContactUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import JsonResponse
from django.db.models import Q
import json
from contacts.selectors import TIP_DOCUMENT, TIP_CONTACT, CATEGORIE_CONTACT
from leads.models import ApartmentLead, HouseLead, TerrainLead, CommercialSpaceLead, OfficeSpaceLead, \
    IndustrialSpaceLead
from listings.models import Apartment, House, Terrain, CommercialSpace, OfficeSpace, IndustrialSpace


class ContactListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Contact
    template_name = 'contacts/contacts.html'
    context_object_name = 'all_contacts'
    permission_required = 'contacts.view_contact'

    def get_queryset(self):
        return Contact.objects.all().order_by('first_name', 'last_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['document_type'] = TIP_DOCUMENT
        context['contact_type'] = TIP_CONTACT
        context['contact_category'] = CATEGORIE_CONTACT
        return context


class ContactUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactUpdateForm
    template_name = 'contacts/edit_contact.html'
    success_url = reverse_lazy('contacts:contact_details')
    permission_required = 'contacts.change_contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['document_type'] = TIP_DOCUMENT
        context['contact_type'] = TIP_CONTACT
        context['contact_category'] = CATEGORIE_CONTACT
        return context

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        return JsonResponse({'errors': errors}, status=400)

    def get_success_url(self):
        return reverse_lazy('contacts:contact_details', kwargs={'pk': self.object.pk})


class ContactDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Contact
    template_name = 'contacts/delete_contact.html'
    success_url = reverse_lazy('contacts:contact_deleted')
    permission_required = 'contacts.delete_contact'


class DeleteContactDoneView(TemplateView):
    template_name = 'contacts/contact_deleted.html'


class ContactDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Contact
    template_name = 'contacts/contact_details.html'
    permission_required = 'contacts.view_contact_details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_listings = []
        all_leads = []

        apartments = Apartment.objects.filter(contact=self.object)
        houses = House.objects.filter(contact=self.object)
        terrains = Terrain.objects.filter(contact=self.object)
        commercial_spaces = CommercialSpace.objects.filter(contact=self.object)
        office_spaces = OfficeSpace.objects.filter(contact=self.object)
        industrial_spaces = IndustrialSpace.objects.filter(contact=self.object)

        apartment_leads = ApartmentLead.objects.filter(contact=self.object)
        house_leads = HouseLead.objects.filter(contact=self.object)
        terrain_leads = TerrainLead.objects.filter(contact=self.object)
        commercial_space_leads = CommercialSpaceLead.objects.filter(contact=self.object)
        office_space_leads = OfficeSpaceLead.objects.filter(contact=self.object)
        industrial_space_leads = IndustrialSpaceLead.objects.filter(contact=self.object)

        all_listings.extend(apartments)
        all_listings.extend(houses)
        all_listings.extend(terrains)
        all_listings.extend(commercial_spaces)
        all_listings.extend(office_spaces)
        all_listings.extend(industrial_spaces)

        all_leads.extend(apartment_leads)
        all_leads.extend(house_leads)
        all_leads.extend(terrain_leads)
        all_leads.extend(commercial_space_leads)
        all_leads.extend(office_space_leads)
        all_leads.extend(industrial_space_leads)

        context['all_listings'] = all_listings
        context['all_leads'] = all_leads
        return context


########################################################################################################################

@login_required
@require_GET
def check_duplicate(request):
    try:
        field_name = request.GET.get('field')
        value = request.GET.get('value')
        current_id = request.GET.get('current_id')

        if value is None or value == '':
            return JsonResponse({'isDuplicate': False})

        if field_name == 'phone_number' and value is not None:
            is_duplicate = Contact.objects.filter(
                Q(phone_number=value) & ~Q(id=current_id)
            ).exists()
        elif field_name == 'email' and value is not None:
            is_duplicate = Contact.objects.filter(
                Q(email=value) & ~Q(id=current_id)
            ).exists()
        else:
            raise ValueError('Câmpul specificat nu poate fi verificat pentru duplicare.')

        return JsonResponse({'isDuplicate': is_duplicate})
    except ValueError as e:
        return JsonResponse({'error': str(e)})


@login_required
@require_POST
def save_contact(request):
    try:
        data = json.loads(request.body.decode('UTF-8'))

        first_name = data.get('first_name')
        last_name = data.get('last_name', None) or None
        phone_number = data.get('phone_number', None) or None
        email = data.get('email', None) or None

        company = data.get('company', None) or None
        job_title = data.get('job_title', None) or None

        city = data.get('city', None) or None
        street_address = data.get('street_address', None) or None
        street_number = data.get('street_number', None) or None
        block = data.get('block', None) or None
        scale = data.get('scale', None) or None
        apartment_number = data.get('apartment_number', None) or None
        county = data.get('county', None) or None
        country = data.get('country', None) or None

        document_type = data.get('document_type', None) or None
        id_series_nr = data.get('id_series_nr', None) or None
        cnp = data.get('cnp', None) or None
        issue_date = data.get('issue_date', None) or None
        passport_country = data.get('passport_country', None) or None

        contact_type = data.get('contact_type', None) or None
        contact_category = data.get('contact_category', None) or None

        other_details = data.get('other_details', None) or None

        if issue_date == 'undefined-undefined-':
            issue_date = None

        if not first_name:
            raise ValueError('Trebuie să introduci obligatoriu un prenume.')

        if not phone_number and not email:
            raise ValueError('Trebuie să introduci obligatoriu cel puțin un număr de telefon sau o adresă de e-mail.')

        if phone_number and not (10 <= len(phone_number) <= 14 and phone_number.isdigit()):
            raise ValueError('Numărul de telefon trebuie să conțină între 10 și 14 cifre legate.')

        is_duplicate_phone = check_duplicate(request, 'phone_number', phone_number, None).get('isDuplicate', False)
        if is_duplicate_phone:
            return JsonResponse({'success': False,
                                 'message': 'Există deja un contact cu acest număr de telefon. '
                                            'Introdu alt număr de telefon sau actualizează contactul existent.'})

        is_duplicate_email = check_duplicate(request, 'email', email, None).get('isDuplicate', False)
        if is_duplicate_email:
            return JsonResponse({'success': False,
                                 'message': 'Există deja un contact cu această adresă de e-mail. '
                                            'Introdu altă adresă de e-mail sau actualizează contactul existent.'})

        if document_type == 'Carte de identitate':
            if not id_series_nr:
                raise ValueError('Seria și numărul cărții de identitate sunt obligatorii.')
            if not id_series_nr.isupper() or not (len(id_series_nr) == 8 or len(id_series_nr) == 9):
                raise ValueError('Seria și numărul cărții de identitate sunt invalide. '
                                 '(ex. corect: "AZ 123456", cu majuscule)')

            if cnp and len(cnp) != 13:
                raise ValueError('CNP-ul este invalid. Acesta trebuie să conțină exact 13 cifre.')

            if not issue_date:
                raise ValueError('Data emiterii cărții de identitate este obligatorie.')

        if document_type == 'Pașaport':
            if not id_series_nr:
                raise ValueError('Numărul pașaportului este obligatoriu.')
            if not id_series_nr.isupper() or not (len(id_series_nr) == 8 or len(id_series_nr) == 9):
                raise ValueError('Numărul pașaportului este invalid. '
                                 '(ex. corect, după caz: "123456789" sau "AZ1234567", cu majuscule)')

            if not issue_date:
                raise ValueError('Data emiterii pașaportului este obligatorie.')

            if not passport_country:
                raise ValueError('Țara emitentă a pașaportului este obligatorie.')

        if document_type == 'Certificat de înregistrare':
            if not cnp:
                raise ValueError('CUI-ul companiei este obligatoriu.')
            if cnp.startswith('RO'):
                cnp_num = cnp[2:]
            else:
                cnp_num = cnp

            if not (7 <= len(cnp_num) <= 8 and cnp_num.isdigit()):
                raise ValueError('CUI-ul este invalid. (ex. corect, după caz: "12345678" sau "RO12345678", '
                                 'cu majuscule.)')
            if not company:
                raise ValueError('Numele companiei este obligatoriu.')
            if not job_title:
                raise ValueError('Funcția în companie este obligatorie.')

        new_contact = Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,

            company=company,
            job_title=job_title,

            city=city,
            street_address=street_address,
            street_number=street_number,
            block=block,
            scale=scale,
            apartment_number=apartment_number,
            county=county,
            country=country,

            document_type=document_type,
            id_series_nr=id_series_nr,
            cnp=cnp,
            issue_date=issue_date,
            passport_country=passport_country,

            contact_type=contact_type,
            contact_category=contact_category,

            other_details=other_details,

            created_by=request.user
        )

        print('Date POST primite:', json.loads(request.body))

        return JsonResponse({'success': True, 'message': 'Contactul a fost salvat cu succes!'})
    except ValueError as e:
        return JsonResponse({'success': False, 'message': str(e)})


@login_required
@require_GET
def get_contact_details(request, contact_id):
    try:
        contact = Contact.objects.get(id=contact_id)
        contact_data = {
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'phone_number': contact.phone_number,
            'email': contact.email,
        }
        return JsonResponse(contact_data)
    except Contact.DoesNotExist:
        return JsonResponse({'error': 'Contactul nu a fost găsit!'}, status=404)
