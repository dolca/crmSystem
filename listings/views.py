from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView
from contacts.models import Contact
from listings.forms import ResidentialEnsembleCreateForm, ResidentialEnsembleUpdateForm, OfficeBuildingCreateForm, \
    OfficeBuildingUpdateForm, ApartmentCreateForm, ApartmentUpdateForm, HouseCreateForm, HouseUpdateForm, \
    TerrainCreateForm, TerrainUpdateForm, CommercialSpaceCreateForm, CommercialSpaceUpdateForm, OfficeSpaceCreateForm, \
    OfficeSpaceUpdateForm, IndustrialSpaceCreateForm, IndustrialSpaceUpdateForm
from listings.models import ResidentialEnsemble, OfficeBuilding, Apartment, House, Terrain, CommercialSpace, \
    OfficeSpace, IndustrialSpace


########################################################################################################################
#                              --- APARTAMENTE ---

class ApartmentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Apartment
    form_class = ApartmentCreateForm
    template_name = 'listings/apartments/add_apartment.html'
    success_url = reverse_lazy('listings:property_added')
    permission_required = 'listings.add_apartment'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.created_by = self.request.user

        return super().form_valid(form)


@login_required
def my_apartments_view(request):
    my_apartments = Apartment.objects.filter(assigned_user=request.user).order_by('-updated_at')
    return render(request, 'listings/apartments/my_apartments.html', {'my_apartments': my_apartments})


class ApartmentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Apartment
    template_name = 'listings/apartments/all_apartments.html'
    context_object_name = 'apartments'
    permission_required = 'listings.view_apartment'

    def get_queryset(self):
        return Apartment.objects.all().order_by('-updated_at')


class ApartmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Apartment
    form_class = ApartmentUpdateForm
    template_name = 'listings/apartments/edit_apartment.html'
    success_url = reverse_lazy('listings:apartment_details')
    permission_required = 'listings.change_apartment'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        update_success = form.save()
        return HttpResponseRedirect(reverse('listings:apartment_details', args=[update_success.pk]))


class ApartmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Apartment
    template_name = 'listings/apartments/delete_apartment.html'
    success_url = reverse_lazy('listings:property_deleted')
    permission_required = 'listings.delete_apartment'


class ApartmentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Apartment
    template_name = 'listings/apartments/apartment_details.html'
    permission_required = 'listings.view_apartment_details'


########################################################################################################################
#                              --- CASE ---

class HouseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = House
    form_class = HouseCreateForm
    template_name = 'listings/houses/add_house.html'
    success_url = reverse_lazy('listings:property_added')
    permission_required = 'listings.add_house'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.created_by = self.request.user

        return super().form_valid(form)


@login_required
def my_houses_view(request):
    my_houses = House.objects.filter(assigned_user=request.user).order_by('-updated_at')
    return render(request, 'listings/houses/my_houses.html', {'my_houses': my_houses})


class HouseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = House
    template_name = 'listings/houses/all_houses.html'
    context_object_name = 'houses'
    permission_required = 'listings.view_house'

    def get_queryset(self):
        return House.objects.all().order_by('-updated_at')


class HouseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = House
    form_class = HouseUpdateForm
    template_name = 'listings/houses/edit_house.html'
    success_url = reverse_lazy('listings:house_details')
    permission_required = 'listings.change_house'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        update_success = form.save()
        return HttpResponseRedirect(reverse('listings:house_details', args=[update_success.pk]))


class HouseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = House
    template_name = 'listings/houses/delete_house.html'
    success_url = reverse_lazy('listings:property_deleted')
    permission_required = 'listings.delete_house'


class HouseDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = House
    template_name = 'listings/houses/house_details.html'
    permission_required = 'listings.view_house_details'


########################################################################################################################
#                              --- TERENURI ---

class TerrainCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Terrain
    form_class = TerrainCreateForm
    template_name = 'listings/terrains/add_terrain.html'
    success_url = reverse_lazy('listings:property_added')
    permission_required = 'listings.add_terrain'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.created_by = self.request.user

        return super().form_valid(form)


@login_required
def my_terrains_view(request):
    my_terrains = Terrain.objects.filter(assigned_user=request.user).order_by('-updated_at')
    return render(request, 'listings/terrains/my_terrains.html', {'my_terrains': my_terrains})


class TerrainListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Terrain
    template_name = 'listings/terrains/all_terrains.html'
    context_object_name = 'terrains'
    permission_required = 'listings.view_terrain'

    def get_queryset(self):
        return Terrain.objects.all().order_by('-updated_at')


class TerrainUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Terrain
    form_class = TerrainUpdateForm
    template_name = 'listings/terrains/edit_terrain.html'
    success_url = reverse_lazy('listings:terrain_details')
    permission_required = 'listings.change_terrain'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        update_success = form.save()
        return HttpResponseRedirect(reverse('listings:terrain_details', args=[update_success.pk]))


class TerrainDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Terrain
    template_name = 'listings/terrains/delete_terrain.html'
    success_url = reverse_lazy('listings:property_deleted')
    permission_required = 'listings.delete_terrain'


class TerrainDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Terrain
    template_name = 'listings/terrains/terrain_details.html'
    permission_required = 'listings.view_terrain_details'


########################################################################################################################
#                              --- SPATII COMERCIALE ---

class CommercialSpaceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CommercialSpace
    form_class = CommercialSpaceCreateForm
    template_name = 'listings/commercial_spaces/add_commercial_space.html'
    success_url = reverse_lazy('listings:property_added')
    permission_required = 'listings.add_commercial_space'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.created_by = self.request.user

        return super().form_valid(form)


@login_required
def my_commercial_spaces_view(request):
    my_commercial_spaces = CommercialSpace.objects.filter(assigned_user=request.user).order_by('-updated_at')
    return render(request, 'listings/commercial_spaces/my_commercial_spaces.html', {
        'my_commercial_spaces': my_commercial_spaces
    })


class CommercialSpaceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CommercialSpace
    template_name = 'listings/commercial_spaces/all_commercial_spaces.html'
    context_object_name = 'commercial_spaces'
    permission_required = 'listings.view_commercial_space'

    def get_queryset(self):
        return CommercialSpace.objects.all().order_by('-updated_at')


class CommercialSpaceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CommercialSpace
    form_class = CommercialSpaceUpdateForm
    template_name = 'listings/commercial_spaces/edit_commercial_space.html'
    success_url = reverse_lazy('listings:commercial_space_details')
    permission_required = 'listings.change_commercial_space'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        update_success = form.save()
        return HttpResponseRedirect(reverse('listings:commercial_space_details', args=[update_success.pk]))


class CommercialSpaceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CommercialSpace
    template_name = 'listings/commercial_spaces/delete_commercial_space.html'
    success_url = reverse_lazy('listings:property_deleted')
    permission_required = 'listings.delete_commercial_space'


class CommercialSpaceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = CommercialSpace
    template_name = 'listings/commercial_spaces/commercial_space_details.html'
    permission_required = 'listings.view_commercial_space_details'


########################################################################################################################
#                              --- SPATII DE BIROURI ---

class OfficeSpaceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = OfficeSpace
    form_class = OfficeSpaceCreateForm
    template_name = 'listings/office_spaces/add_office_space.html'
    success_url = reverse_lazy('listings:property_added')
    permission_required = 'listings.add_office_space'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.created_by = self.request.user

        return super().form_valid(form)


@login_required
def my_office_spaces_view(request):
    my_office_spaces = OfficeSpace.objects.filter(assigned_user=request.user).order_by('-updated_at')
    return render(request, 'listings/office_spaces/my_office_spaces.html', {
        'my_office_spaces': my_office_spaces
    })


class OfficeSpaceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = OfficeSpace
    template_name = 'listings/office_spaces/all_office_spaces.html'
    context_object_name = 'office_spaces'
    permission_required = 'listings.view_office_space'

    def get_queryset(self):
        return OfficeSpace.objects.all().order_by('-updated_at')


class OfficeSpaceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = OfficeSpace
    form_class = OfficeSpaceUpdateForm
    template_name = 'listings/office_spaces/edit_office_space.html'
    success_url = reverse_lazy('listings:office_space_details')
    permission_required = 'listings.change_office_space'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        update_success = form.save()
        return HttpResponseRedirect(reverse('listings:office_space_details', args=[update_success.pk]))


class OfficeSpaceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = OfficeSpace
    template_name = 'listings/office_spaces/delete_office_space.html'
    success_url = reverse_lazy('listings:property_deleted')
    permission_required = 'listings.delete_office_space'


class OfficeSpaceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = OfficeSpace
    template_name = 'listings/office_spaces/office_space_details.html'
    permission_required = 'listings.view_office_space_details'


########################################################################################################################
#                              --- SPATII INDUSTRIALE ---

class IndustrialSpaceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = IndustrialSpace
    form_class = IndustrialSpaceCreateForm
    template_name = 'listings/industrial_spaces/add_industrial_space.html'
    success_url = reverse_lazy('listings:property_added')
    permission_required = 'listings.add_industrial_space'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.created_by = self.request.user

        return super().form_valid(form)


@login_required
def my_industrial_spaces_view(request):
    my_industrial_spaces = IndustrialSpace.objects.filter(assigned_user=request.user).order_by('-updated_at')
    return render(request, 'listings/industrial_spaces/my_industrial_spaces.html', {
        'my_industrial_spaces': my_industrial_spaces
    })


class IndustrialSpaceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = IndustrialSpace
    template_name = 'listings/industrial_spaces/all_industrial_spaces.html'
    context_object_name = 'industrial_spaces'
    permission_required = 'listings.view_industrial_space'

    def get_queryset(self):
        return IndustrialSpace.objects.all().order_by('-updated_at')


class IndustrialSpaceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = IndustrialSpace
    form_class = IndustrialSpaceUpdateForm
    template_name = 'listings/industrial_spaces/edit_industrial_space.html'
    success_url = reverse_lazy('listings:industrial_space_details')
    permission_required = 'listings.change_industrial_space'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        update_success = form.save()
        return HttpResponseRedirect(reverse('listings:industrial_space_details', args=[update_success.pk]))


class IndustrialSpaceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = IndustrialSpace
    template_name = 'listings/industrial_spaces/delete_industrial_space.html'
    success_url = reverse_lazy('listings:property_deleted')
    permission_required = 'listings.delete_industrial_space'


class IndustrialSpaceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = IndustrialSpace
    template_name = 'listings/industrial_spaces/industrial_space_details.html'
    permission_required = 'listings.view_industrial_space_details'


########################################################################################################################
#                              --- ANSAMBLURI REZIDENTIALE ---

class ResidentialEnsembleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ResidentialEnsemble
    form_class = ResidentialEnsembleCreateForm
    template_name = 'listings/residential_ensembles/add_residential_ensemble.html'
    success_url = reverse_lazy('listings:property_added')
    permission_required = 'listings.add_residential_ensemble'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.created_by = self.request.user

        return super().form_valid(form)


class ResidentialEnsembleListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ResidentialEnsemble
    template_name = 'listings/residential_ensembles/residential_ensembles_list.html'
    context_object_name = 'residential_ensembles'
    permission_required = 'listings.view_residential_ensemble'

    def get_queryset(self):
        return ResidentialEnsemble.objects.all().order_by('-updated_at')


class ResidentialEnsembleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ResidentialEnsemble
    form_class = ResidentialEnsembleUpdateForm
    template_name = 'listings/residential_ensembles/edit_residential_ensemble.html'
    success_url = reverse_lazy('listings:residential_ensemble_details')
    permission_required = 'listings.change_residential_ensemble'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        update_success = form.save()
        return HttpResponseRedirect(reverse('listings:residential_ensemble_details', args=[update_success.pk]))


class ResidentialEnsembleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ResidentialEnsemble
    template_name = 'listings/residential_ensembles/delete_residential_ensemble.html'
    success_url = reverse_lazy('listings:property_deleted')
    permission_required = 'listings.delete_residential_ensemble'


class ResidentialEnsembleDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = ResidentialEnsemble
    template_name = 'listings/residential_ensembles/residential_ensemble_details.html'
    permission_required = 'listings.view_residential_ensemble_details'


########################################################################################################################
#                              --- CLADIRI DE BIROURI ---

class OfficeBuildingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = OfficeBuilding
    form_class = OfficeBuildingCreateForm
    template_name = 'listings/office_buildings/add_office_building.html'
    success_url = reverse_lazy('listings:property_added')
    permission_required = 'listings.add_office_building'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        form.instance.created_by = self.request.user

        return super().form_valid(form)


class OfficeBuildingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = OfficeBuilding
    template_name = 'listings/office_buildings/office_buildings_list.html'
    context_object_name = 'office_buildings'
    permission_required = 'listings.view_office_building'

    def get_queryset(self):
        return OfficeBuilding.objects.all().order_by('-updated_at')


class OfficeBuildingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = OfficeBuilding
    form_class = OfficeBuildingUpdateForm
    template_name = 'listings/office_buildings/edit_office_building.html'
    success_url = reverse_lazy('listings:office_building_details')
    permission_required = 'listings.change_office_building'

    def form_valid(self, form):
        try:
            form.clean()
        except ValidationError as err:
            form.add_error('field_name', str(err))
            return self.form_invalid(form)

        update_success = form.save()
        return HttpResponseRedirect(reverse('listings:office_building_details', args=[update_success.pk]))


class OfficeBuildingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = OfficeBuilding
    template_name = 'listings/office_buildings/delete_office_building.html'
    success_url = reverse_lazy('listings:property_deleted')
    permission_required = 'listings.delete_office_building'


class OfficeBuildingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = OfficeBuilding
    template_name = 'listings/office_buildings/office_building_details.html'
    permission_required = 'listings.view_office_building_details'


########################################################################################################################

class CreatePropertyDoneView(TemplateView):
    template_name = 'listings/property_added.html'


class DeletePropertyDoneView(TemplateView):
    template_name = 'listings/property_deleted.html'


def add_new_property(request):
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

    form = ApartmentCreateForm()
    return render(request, 'listings/add_new_property.html', {'form': form, 'contacts': contacts})
