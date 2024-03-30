from django.urls import path
from leads.views import ApartmentLeadCreateView, my_apartment_leads_view, general_apartment_leads_view, \
    ApartmentLeadListView, ApartmentLeadUpdateView, ApartmentLeadDeleteView, ApartmentLeadDetailView, \
    HouseLeadCreateView, my_house_leads_view, general_house_leads_view, HouseLeadListView, HouseLeadUpdateView, \
    HouseLeadDeleteView, HouseLeadDetailView, TerrainLeadCreateView, my_terrain_leads_view, general_terrain_leads_view, \
    TerrainLeadListView, TerrainLeadUpdateView, TerrainLeadDeleteView, TerrainLeadDetailView, \
    CommercialSpaceLeadCreateView, my_commercial_space_leads_view, general_commercial_space_leads_view, \
    CommercialSpaceLeadListView, CommercialSpaceLeadUpdateView, CommercialSpaceLeadDeleteView, \
    CommercialSpaceLeadDetailView, OfficeSpaceLeadCreateView, my_office_space_leads_view, \
    general_office_space_leads_view, OfficeSpaceLeadListView, OfficeSpaceLeadUpdateView, OfficeSpaceLeadDeleteView, \
    OfficeSpaceLeadDetailView, IndustrialSpaceLeadCreateView, my_industrial_space_leads_view, \
    general_industrial_space_leads_view, IndustrialSpaceLeadListView, IndustrialSpaceLeadUpdateView, \
    IndustrialSpaceLeadDeleteView, IndustrialSpaceLeadDetailView, CreateLeadDoneView, DeleteLeadDoneView, add_new_lead

app_name = 'leads'

urlpatterns = [
    path('add-apartment-lead', ApartmentLeadCreateView.as_view(), name='add_apartment_lead'),
    path('my-apartment-leads', my_apartment_leads_view, name='my_apartment_leads'),
    path('general-apartment-leads', general_apartment_leads_view, name='general_apartment_leads'),
    path('all-apartment-leads', ApartmentLeadListView.as_view(), name='all_apartment_leads'),
    path('edit-apartment-lead/<int:pk>', ApartmentLeadUpdateView.as_view(), name='edit_apartment_lead'),
    path('delete-apartment-lead/<int:pk>', ApartmentLeadDeleteView.as_view(), name='delete_apartment_lead'),
    path('apartment-lead-details/<int:pk>', ApartmentLeadDetailView.as_view(), name='apartment_lead_details'),

    path('add-house-lead', HouseLeadCreateView.as_view(), name='add_house_lead'),
    path('my-house-leads', my_house_leads_view, name='my_house_leads'),
    path('general-house-leads', general_house_leads_view, name='general_house_leads'),
    path('all-house-leads', HouseLeadListView.as_view(), name='all_house_leads'),
    path('edit-house-lead/<int:pk>', HouseLeadUpdateView.as_view(), name='edit_house_lead'),
    path('delete-house-lead/<int:pk>', HouseLeadDeleteView.as_view(), name='delete_house_lead'),
    path('house-lead-details/<int:pk>', HouseLeadDetailView.as_view(), name='house_lead_details'),

    path('add-terrain-lead', TerrainLeadCreateView.as_view(), name='add_terrain_lead'),
    path('my-terrain-leads', my_terrain_leads_view, name='my_terrain_leads'),
    path('general-terrain-leads', general_terrain_leads_view, name='general_terrain_leads'),
    path('all-terrain-leads/', TerrainLeadListView.as_view(), name='all_terrain_leads'),
    path('edit-terrain-lead/<int:pk>', TerrainLeadUpdateView.as_view(), name='edit_terrain_lead'),
    path('delete-terrain-lead/<int:pk>', TerrainLeadDeleteView.as_view(), name='delete_terrain_lead'),
    path('terrain-lead-details/<int:pk>', TerrainLeadDetailView.as_view(), name='terrain_lead_details'),

    path('add-commercial-space-lead', CommercialSpaceLeadCreateView.as_view(), name='add_commercial_space_lead'),
    path('my-commercial-space-leads', my_commercial_space_leads_view, name='my_commercial_space_leads'),
    path('general-commercial-space-leads', general_commercial_space_leads_view, name='general_commercial_space_leads'),
    path('all-commercial-space-leads', CommercialSpaceLeadListView.as_view(), name='all_commercial_space_leads'),
    path('edit-commercial-space-lead/<int:pk>', CommercialSpaceLeadUpdateView.as_view(), name='edit_commercial_space_lead'),
    path('delete-commercial-space-lead/<int:pk>', CommercialSpaceLeadDeleteView.as_view(), name='delete_commercial_space_lead'),
    path('commercial-space-lead-details/<int:pk>', CommercialSpaceLeadDetailView.as_view(), name='commercial_space_lead_details'),

    path('add-office-space-lead', OfficeSpaceLeadCreateView.as_view(), name='add_office_space_lead'),
    path('my-office-space-leads', my_office_space_leads_view, name='my_office_space_leads'),
    path('general-office-space-leads', general_office_space_leads_view, name='general_office_space_leads'),
    path('all-office-space-leads', OfficeSpaceLeadListView.as_view(), name='all_office_space_leads'),
    path('edit-office-space-lead/<int:pk>', OfficeSpaceLeadUpdateView.as_view(), name='edit_office_space_lead'),
    path('delete-office-space-lead/<int:pk>', OfficeSpaceLeadDeleteView.as_view(), name='delete_office_space_lead'),
    path('office-space-lead-details/<int:pk>', OfficeSpaceLeadDetailView.as_view(), name='office_space_lead_details'),

    path('add-industrial-space-lead', IndustrialSpaceLeadCreateView.as_view(), name='add_industrial_space_lead'),
    path('my-industrial-space-leads', my_industrial_space_leads_view, name='my_industrial_space_leads'),
    path('general-industrial-space-leads', general_industrial_space_leads_view, name='general_industrial_space_leads'),
    path('all-industrial-space-leads', IndustrialSpaceLeadListView.as_view(), name='all_industrial_space_leads'),
    path('edit-industrial-space-lead/<int:pk>', IndustrialSpaceLeadUpdateView.as_view(), name='edit_industrial_space_lead'),
    path('delete-industrial-space-lead/<int:pk>', IndustrialSpaceLeadDeleteView.as_view(), name='delete_industrial_space_lead'),
    path('industrial-space-lead-details/<int:pk>', IndustrialSpaceLeadDetailView.as_view(), name='industrial_space_lead_details'),

    path('lead-added', CreateLeadDoneView.as_view(), name='lead_added'),
    path('lead-deleted', DeleteLeadDoneView.as_view(), name='lead_deleted'),

    path('add-new-lead', add_new_lead, name='add_new_lead'),
]
