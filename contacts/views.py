import re
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils import timezone
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
        form.instance.updated_at = timezone.now()

        instance = form.save(commit=False)
        instance.created_by = Contact.objects.get(pk=instance.pk).created_by

        instance.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

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
        elif field_name == 'id_series_nr' and value is not None:
            is_duplicate = Contact.objects.filter(
                Q(id_series_nr=value) & ~Q(id=current_id)
            ).exists()
        elif field_name == 'cnp' and value is not None:
            is_duplicate = Contact.objects.filter(
                Q(cnp=value) & ~Q(id=current_id)
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
            raise ValueError('Numărul de telefon trebuie să conțină între 10 și 14 cifre.')

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
            elif not re.match(r'^[A-Z]{2}\d{6}$', id_series_nr):
                raise ValueError('Seria și numărul cărții de identitate trebuie să conțină codul județului '
                                 'format din 2 litere, cu majuscule, urmat de 6 cifre.')
            is_duplicate_id_series_number = (check_duplicate(request, 'id_series_nr', id_series_nr, None).
                                             get('isDuplicate', False))
            if is_duplicate_id_series_number:
                return JsonResponse({'success': False,
                                     'message': 'Există deja un contact cu aceste date pentru serie și număr. '
                                                'Introdu alte date sau actualizează contactul existent.'})

            if cnp and len(cnp) != 13:
                raise ValueError('CNP-ul trebuie să conțină exact 13 cifre.')
            is_duplicate_cnp = (check_duplicate(request, 'cnp', cnp, None).get('isDuplicate', False))
            if is_duplicate_cnp:
                return JsonResponse({'success': False,
                                     'message': 'Există deja un contact cu acest CNP. '
                                                'Introdu alt CNP sau actualizează contactul existent.'})

            if not issue_date:
                raise ValueError('Data emiterii cărții de identitate este obligatorie.')

        if document_type == 'Pașaport':
            if not id_series_nr:
                raise ValueError('Numărul pașaportului este obligatoriu.')
            if not (6 <= len(id_series_nr) <= 9):
                raise ValueError('Numărul pașaportului trebuie să conțină între 6 și 9 caractere.')
            is_duplicate_pass_number = (check_duplicate(request, 'id_series_nr', id_series_nr, None).
                                        get('isDuplicate', False))
            if is_duplicate_pass_number:
                return JsonResponse({'success': False,
                                     'message': 'Există deja un contact cu acest număr de pașaport. '
                                                'Introdu alt număr de pașaport sau actualizează contactul existent.'})

            if not issue_date:
                raise ValueError('Data emiterii pașaportului este obligatorie.')

            if not passport_country:
                raise ValueError('Țara emitentă a pașaportului este obligatorie.')

        if document_type == 'Certificat de înregistrare':
            if not company:
                raise ValueError('Numele companiei este obligatoriu.')

            if not job_title:
                raise ValueError('Funcția în companie este obligatorie.')

            if not cnp:
                raise ValueError('CUI-ul companiei este obligatoriu.')

            if cnp.startswith('RO'):
                cnp_num = cnp[2:]
            else:
                cnp_num = cnp

            if not (7 <= len(cnp_num) <= 9 and cnp_num.isdigit()):
                raise ValueError(
                    'CUI-ul trebuie să conțină între 7 și 9 cifre, cu prefixul "RO" pentru plătitorii de TVA.')
            is_duplicate_cui = (check_duplicate(request, 'cnp', cnp, None).get('isDuplicate', False))
            if is_duplicate_cui:
                return JsonResponse({'success': False,
                                     'message': 'Există deja un contact cu acest CUI. '
                                                'Introdu alt CUI sau actualizează contactul existent.'})

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
            'company': contact.company,
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'phone_number': contact.phone_number,
            'email': contact.email,
        }
        return JsonResponse(contact_data)
    except Contact.DoesNotExist:
        return JsonResponse({'error': 'Contactul nu a fost găsit!'}, status=404)
