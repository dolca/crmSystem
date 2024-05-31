from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView
from contacts.models import Contact
from leads.forms import ApartmentLeadCreateForm, ApartmentLeadUpdateForm, HouseLeadCreateForm, HouseLeadUpdateForm, \
    TerrainLeadCreateForm, TerrainLeadUpdateForm, CommercialSpaceLeadCreateForm, CommercialSpaceLeadUpdateForm, \
    OfficeSpaceLeadCreateForm, OfficeSpaceLeadUpdateForm, IndustrialSpaceLeadCreateForm, IndustrialSpaceLeadUpdateForm
from leads.models import ApartmentLead, HouseLead, TerrainLead, CommercialSpaceLead, OfficeSpaceLead, \
    IndustrialSpaceLead


########################################################################################################################
#                              --- APARTAMENTE ---

class ApartmentLeadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ApartmentLead
    form_class = ApartmentLeadCreateForm
    template_name = 'leads/apartments/add_apartment_lead.html'
    success_url = reverse_lazy('leads:lead_added')
    permission_required = 'leads.add_apartmentlead'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stored_contact = self.request.session.get('storedContactId')
        stored_type = self.request.session.get('storedType')
        context['storedContactId'] = stored_contact
        context['storedType'] = stored_type
        return context

    def form_valid(self, form):
        form.instance.created_at = timezone.now()
        form.instance.updated_at = timezone.now()
        form.instance.created_by = self.request.user

        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        return JsonResponse({'errors': errors}, status=400)


@login_required
def my_apartment_leads_view(request):
    my_apartment_leads = ApartmentLead.objects.filter(created_by=request.user).order_by('-deadline_date')
    return render(request, 'leads/apartments/my_apartment_leads.html', {
        'my_apartment_leads': my_apartment_leads
    })


@login_required
def general_apartment_leads_view(request):
    general_apartment_leads = ApartmentLead.objects.filter(assigned_listings__isnull=True).order_by('-updated_at')
    return render(request, 'leads/apartments/general_apartment_leads.html', {
        'general_apartment_leads': general_apartment_leads
    })


class ApartmentLeadListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ApartmentLead
    template_name = 'leads/apartments/all_apartment_leads.html'
    context_object_name = 'all_apartment_leads'
    permission_required = 'leads.view_apartmentlead'

    def get_queryset(self):
        return ApartmentLead.objects.all().order_by('-updated_at')


class ApartmentLeadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ApartmentLead
    form_class = ApartmentLeadUpdateForm
    template_name = 'leads/apartments/edit_apartment_lead.html'
    permission_required = 'leads.change_apartmentlead'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def form_valid(self, form):
        form.instance.updated_at = timezone.now()
        form.instance.updated_by = self.request.user

        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        return JsonResponse({'errors': errors}, status=400)

    def get_success_url(self):
        return reverse_lazy('leads:apartment_lead_details', kwargs={'pk': self.object.pk})


class ApartmentLeadDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ApartmentLead
    template_name = 'leads/apartments/delete_apartment_lead.html'
    success_url = reverse_lazy('leads:lead_deleted')
    permission_required = 'leads.delete_apartmentlead'


class ApartmentLeadDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = ApartmentLead
    template_name = 'leads/apartments/apartment_lead_details.html'
    permission_required = 'leads.view_apartmentlead_details'


########################################################################################################################
#                              --- CASE ---

class HouseLeadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = HouseLead
    form_class = HouseLeadCreateForm
    template_name = 'leads/houses/add_house_lead.html'
    success_url = reverse_lazy('leads:lead_added')
    permission_required = 'leads.add_house_lead'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        return super().form_valid(form)


@login_required
def my_house_leads_view(request):
    my_house_leads = HouseLead.objects.filter(created_by=request.user).order_by('-deadline_date')
    return render(request, 'leads/houses/my_house_leads.html', {'my_house_leads': my_house_leads})


@login_required
def general_house_leads_view(request):
    general_house_leads = HouseLead.objects.filter(assigned_listings__isnull=True).order_by('-updated_at')
    return render(request, 'leads/houses/general_house_leads.html', {
        'general_house_leads': general_house_leads
    })


class HouseLeadListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = HouseLead
    template_name = 'leads/houses/all_house_leads.html'
    context_object_name = 'all_house_leads'
    permission_required = 'leads.view_house_lead'

    def get_queryset(self):
        return HouseLead.objects.all().order_by('-updated_at')


class HouseLeadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = HouseLead
    form_class = HouseLeadUpdateForm
    template_name = 'leads/houses/edit_house_lead.html'
    success_url = reverse_lazy('leads:house_lead_details')
    permission_required = 'leads.change_house_lead'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.updated_by = self.request.user

        update_success = form.save()
        return HttpResponseRedirect(reverse('leads:house_lead_details', args=[update_success.pk]))


class HouseLeadDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = HouseLead
    template_name = 'leads/houses/delete_house_lead.html'
    success_url = reverse_lazy('leads:lead_deleted')
    permission_required = 'leads.delete_house_lead'


class HouseLeadDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = HouseLead
    template_name = 'leads/houses/house_lead_details.html'
    permission_required = 'leads.view_house_lead_details'


########################################################################################################################
#                              --- TERENURI ---

class TerrainLeadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TerrainLead
    form_class = TerrainLeadCreateForm
    template_name = 'leads/terrains/add_terrain_lead.html'
    success_url = reverse_lazy('leads:lead_added')
    permission_required = 'leads.add_terrain_lead'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        return super().form_valid(form)


@login_required
def my_terrain_leads_view(request):
    my_terrain_leads = TerrainLead.objects.filter(created_by=request.user).order_by('-deadline_date')
    return render(request, 'leads/terrains/my_terrain_leads.html', {
        'my_terrain_leads': my_terrain_leads
    })


@login_required
def general_terrain_leads_view(request):
    general_terrain_leads = TerrainLead.objects.filter(assigned_listings__isnull=True).order_by('-updated_at')
    return render(request, 'leads/terrains/general_terrain_leads.html', {
        'general_terrain_leads': general_terrain_leads
    })


class TerrainLeadListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = TerrainLead
    template_name = 'leads/terrains/all_terrain_leads.html'
    context_object_name = 'all_terrain_leads'
    permission_required = 'leads.view_terrain_lead'

    def get_queryset(self):
        return TerrainLead.objects.all().order_by('-updated_at')


class TerrainLeadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TerrainLead
    form_class = TerrainLeadUpdateForm
    template_name = 'leads/terrains/edit_terrain_lead.html'
    success_url = reverse_lazy('leads:terrain_lead_details')
    permission_required = 'leads.change_terrain_lead'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.updated_by = self.request.user

        update_success = form.save()
        return HttpResponseRedirect(reverse('leads:terrain_lead_details', args=[update_success.pk]))


class TerrainLeadDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = TerrainLead
    template_name = 'leads/terrains/delete_terrain_lead.html'
    success_url = reverse_lazy('leads:lead_deleted')
    permission_required = 'leads.delete_terrain_lead'


class TerrainLeadDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = TerrainLead
    template_name = 'leads/terrains/terrain_lead_details.html'
    permission_required = 'leads.view_terrain_lead_details'


########################################################################################################################
#                              --- SPATII COMERCIALE ---

class CommercialSpaceLeadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CommercialSpaceLead
    form_class = CommercialSpaceLeadCreateForm
    template_name = 'leads/commercial_spaces/add_commercial_space_lead.html'
    success_url = reverse_lazy('leads:lead_added')
    permission_required = 'leads.add_commercial_space_lead'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        return super().form_valid(form)


@login_required
def my_commercial_space_leads_view(request):
    my_commercial_space_leads = CommercialSpaceLead.objects.filter(created_by=request.user).order_by('-deadline_date')
    return render(request, 'leads/commercial_spaces/my_commercial_space_leads.html', {
        'my_commercial_space_leads': my_commercial_space_leads
    })


@login_required
def general_commercial_space_leads_view(request):
    general_commercial_space_leads = CommercialSpaceLead.objects.filter(assigned_listings__isnull=True).order_by('-updated_at')
    return render(request, 'leads/commercial_spaces/general_commercial_space_leads.html', {
        'general_commercial_space_leads': general_commercial_space_leads
    })


class CommercialSpaceLeadListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CommercialSpaceLead
    template_name = 'leads/commercial_spaces/all_commercial_space_leads.html'
    context_object_name = 'all_commercial_space_leads'
    permission_required = 'leads.view_commercial_space_lead'

    def get_queryset(self):
        return CommercialSpaceLead.objects.all().order_by('-updated_at')


class CommercialSpaceLeadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CommercialSpaceLead
    form_class = CommercialSpaceLeadUpdateForm
    template_name = 'leads/commercial_spaces/edit_commercial_space_lead.html'
    success_url = reverse_lazy('leads:commercial_space_lead_details')
    permission_required = 'leads.change_commercial_space_lead'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.updated_by = self.request.user

        update_success = form.save()
        return HttpResponseRedirect(reverse('leads:commercial_space_lead_details', args=[update_success.pk]))


class CommercialSpaceLeadDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CommercialSpaceLead
    template_name = 'leads/commercial_spaces/delete_commercial_space_lead.html'
    success_url = reverse_lazy('leads:lead_deleted')
    permission_required = 'leads.delete_commercial_space_lead'


class CommercialSpaceLeadDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = CommercialSpaceLead
    template_name = 'leads/commercial_spaces/commercial_space_lead_details.html'
    permission_required = 'leads.view_commercial_space_lead_details'


########################################################################################################################
#                              --- SPATII DE BIROURI ---

class OfficeSpaceLeadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = OfficeSpaceLead
    form_class = OfficeSpaceLeadCreateForm
    template_name = 'leads/office_spaces/add_office_space_lead.html'
    success_url = reverse_lazy('leads:lead_added')
    permission_required = 'leads.add_office_space_lead'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        return super().form_valid(form)


@login_required
def my_office_space_leads_view(request):
    my_office_space_leads = OfficeSpaceLead.objects.filter(created_by=request.user).order_by('-deadline_date')
    return render(request, 'leads/office_spaces/my_office_space_leads.html', {
        'my_office_space_leads': my_office_space_leads
    })


@login_required
def general_office_space_leads_view(request):
    general_office_space_leads = (OfficeSpaceLead.objects.filter(assigned_listings__isnull=True).order_by('-updated_at'))
    return render(request, 'leads/office_spaces/general_office_space_leads.html', {
        'general_office_space_leads': general_office_space_leads
    })


class OfficeSpaceLeadListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = OfficeSpaceLead
    template_name = 'leads/office_spaces/all_office_space_leads.html'
    context_object_name = 'all_office_space_leads'
    permission_required = 'leads.view_office_space_lead'

    def get_queryset(self):
        return OfficeSpaceLead.objects.all().order_by('-updated_at')


class OfficeSpaceLeadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = OfficeSpaceLead
    form_class = OfficeSpaceLeadUpdateForm
    template_name = 'leads/office_spaces/edit_office_space_lead.html'
    success_url = reverse_lazy('leads:office_space_lead_details')
    permission_required = 'leads.change_office_space_lead'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.updated_by = self.request.user

        update_success = form.save()
        return HttpResponseRedirect(reverse('leads:office_space_lead_details', args=[update_success.pk]))


class OfficeSpaceLeadDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = OfficeSpaceLead
    template_name = 'leads/office_spaces/delete_office_space_lead.html'
    success_url = reverse_lazy('leads:lead_deleted')
    permission_required = 'leads.delete_office_space_lead'


class OfficeSpaceLeadDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = OfficeSpaceLead
    template_name = 'leads/office_spaces/office_space_lead_details.html'
    permission_required = 'leads.view_office_space_lead_details'


########################################################################################################################
#                              --- SPATII INDUSTRIALE ---

class IndustrialSpaceLeadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = IndustrialSpaceLead
    form_class = IndustrialSpaceLeadCreateForm
    template_name = 'leads/industrial_spaces/add_industrial_space_lead.html'
    success_url = reverse_lazy('leads:lead_added')
    permission_required = 'leads.add_industrial_space_lead'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        return super().form_valid(form)


@login_required
def my_industrial_space_leads_view(request):
    my_industrial_space_leads = IndustrialSpaceLead.objects.filter(created_by=request.user).order_by('-deadline_date')
    return render(request, 'leads/industrial_spaces/my_industrial_space_leads.html', {
        'my_industrial_space_leads': my_industrial_space_leads
    })


@login_required
def general_industrial_space_leads_view(request):
    general_industrial_space_leads = IndustrialSpaceLead.objects.filter(assigned_listings__isnull=True).order_by('-updated_at')
    return render(request, 'leads/industrial_spaces/general_industrial_space_leads.html', {
        'general_industrial_space_leads': general_industrial_space_leads
    })


class IndustrialSpaceLeadListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = IndustrialSpaceLead
    template_name = 'leads/industrial_spaces/all_industrial_space_leads.html'
    context_object_name = 'all_industrial_space_leads'
    permission_required = 'leads.view_industrial_space_lead'

    def get_queryset(self):
        return IndustrialSpaceLead.objects.all().order_by('-updated_at')


class IndustrialSpaceLeadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = IndustrialSpaceLead
    form_class = IndustrialSpaceLeadUpdateForm
    template_name = 'leads/industrial_spaces/edit_industrial_space_lead.html'
    success_url = reverse_lazy('leads:industrial_space_lead_details')
    permission_required = 'leads.change_industrial_space_lead'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.updated_by = self.request.user

        update_success = form.save()
        return HttpResponseRedirect(reverse('leads:industrial_space_lead_details', args=[update_success.pk]))


class IndustrialSpaceLeadDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = IndustrialSpaceLead
    template_name = 'leads/industrial_spaces/delete_industrial_space_lead.html'
    success_url = reverse_lazy('leads:lead_deleted')
    permission_required = 'leads.delete_industrial_space_lead'


class IndustrialSpaceLeadDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = IndustrialSpaceLead
    template_name = 'leads/industrial_spaces/industrial_space_lead_details.html'
    permission_required = 'leads.view_industrial_space_lead_details'


########################################################################################################################

class CreateLeadDoneView(TemplateView):
    template_name = 'leads/lead_added.html'


class DeleteLeadDoneView(TemplateView):
    template_name = 'leads/lead_deleted.html'


def add_new_lead(request):
    contacts = Contact.objects.all()

    if request.method == 'POST':
        contact_id = request.POST.get('id_contact')
        property_type = request.POST.get('id_property_type')

        if property_type == 'Apartament':
            return redirect(reverse('leads:add_apartment_lead') + f'?id_contact={contact_id}')
        elif property_type == 'Casă':
            return redirect(reverse('leads:add_house_lead') + f'?id_contact={contact_id}')
        elif property_type == 'Teren':
            return redirect(reverse('leads:add_terrain_lead') + f'?id_contact={contact_id}')
        elif property_type == 'Spațiu comercial':
            return redirect(reverse('leads:add_commercial_space_lead') + f'?id_contact={contact_id}')
        elif property_type == 'Spațiu de birouri':
            return redirect(reverse('leads:add_office_space_lead') + f'?id_contact={contact_id}')
        elif property_type == 'Spațiu industrial':
            return redirect(reverse('leads:add_industrial_space_lead') + f'?id_contact={contact_id}')

    form = ApartmentLeadCreateForm()
    return render(request, 'leads/add_new_lead.html', {'form': form, 'contacts': contacts})
