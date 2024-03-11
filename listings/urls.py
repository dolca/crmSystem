from django.urls import path
from listings.views import ResidentialEnsembleCreateView, ResidentialEnsembleListView, ResidentialEnsembleUpdateView, \
    ResidentialEnsembleDeleteView, ResidentialEnsembleDetailView, OfficeBuildingCreateView, OfficeBuildingListView, \
    OfficeBuildingUpdateView, OfficeBuildingDeleteView, OfficeBuildingDetailView, ApartmentCreateView, \
    my_apartments_view, ApartmentListView, ApartmentUpdateView, ApartmentDeleteView, ApartmentDetailView, \
    HouseCreateView, my_houses_view, HouseListView, HouseUpdateView, HouseDeleteView, HouseDetailView, \
    TerrainCreateView, my_terrains_view, TerrainListView, TerrainUpdateView, TerrainDeleteView, TerrainDetailView, \
    CommercialSpaceCreateView, my_commercial_spaces_view, CommercialSpaceListView, CommercialSpaceUpdateView, \
    CommercialSpaceDeleteView, CommercialSpaceDetailView, OfficeSpaceCreateView, my_office_spaces_view, \
    OfficeSpaceListView, OfficeSpaceUpdateView, OfficeSpaceDeleteView, OfficeSpaceDetailView, IndustrialSpaceCreateView, \
    my_industrial_spaces_view, IndustrialSpaceListView, IndustrialSpaceUpdateView, IndustrialSpaceDeleteView, \
    IndustrialSpaceDetailView, CreatePropertyDoneView, DeletePropertyDoneView, add_new_property

app_name = 'listings'

urlpatterns = [
    path('add-apartment/', ApartmentCreateView.as_view(), name='add_apartment'),
    path('my-apartments/', my_apartments_view, name='my_apartments'),
    path('all-apartments/', ApartmentListView.as_view(), name='all_apartments'),
    path('edit-apartment/<int:pk>', ApartmentUpdateView.as_view(), name='edit_apartment'),
    path('delete-apartment/<int:pk>/', ApartmentDeleteView.as_view(), name='delete_apartment'),
    path('apartment-details/<int:pk>', ApartmentDetailView.as_view(), name='apartment_details'),

    path('add-house/', HouseCreateView.as_view(), name='add_house'),
    path('my-houses/', my_houses_view, name='my_houses'),
    path('all-houses/', HouseListView.as_view(), name='all_houses'),
    path('edit-house/<int:pk>', HouseUpdateView.as_view(), name='edit_house'),
    path('delete-house/<int:pk>/', HouseDeleteView.as_view(), name='delete_house'),
    path('house-details/<int:pk>', HouseDetailView.as_view(), name='house_details'),

    path('add-terrain/', TerrainCreateView.as_view(), name='add_terrain'),
    path('my-terrains/', my_terrains_view, name='my_terrains'),
    path('all-terrains/', TerrainListView.as_view(), name='all_terrains'),
    path('edit-terrain/<int:pk>', TerrainUpdateView.as_view(), name='edit_terrain'),
    path('delete-terrain/<int:pk>/', TerrainDeleteView.as_view(), name='delete_terrain'),
    path('terrain-details/<int:pk>', TerrainDetailView.as_view(), name='terrain_details'),

    path('add-commercial-space/', CommercialSpaceCreateView.as_view(), name='add_commercial_space'),
    path('my-commercial-spaces/', my_commercial_spaces_view, name='my_commercial_spaces'),
    path('all-commercial-spaces/', CommercialSpaceListView.as_view(), name='all_commercial_spaces'),
    path('edit-commercial-space/<int:pk>', CommercialSpaceUpdateView.as_view(), name='edit_commercial_space'),
    path('delete-commercial-space/<int:pk>/', CommercialSpaceDeleteView.as_view(), name='delete_commercial_space'),
    path('commercial-space-details/<int:pk>', CommercialSpaceDetailView.as_view(), name='commercial_space_details'),

    path('add-office-space/', OfficeSpaceCreateView.as_view(), name='add_office_space'),
    path('my-office-spaces/', my_office_spaces_view, name='my_office_spaces'),
    path('all-office-spaces/', OfficeSpaceListView.as_view(), name='all_office_spaces'),
    path('edit-office-space/<int:pk>', OfficeSpaceUpdateView.as_view(), name='edit_office_space'),
    path('delete-office-space/<int:pk>/', OfficeSpaceDeleteView.as_view(), name='delete_office_space'),
    path('office-space-details/<int:pk>', OfficeSpaceDetailView.as_view(), name='office_space_details'),

    path('add-industrial-space/', IndustrialSpaceCreateView.as_view(), name='add_industrial_space'),
    path('my-industrial-spaces/', my_industrial_spaces_view, name='my_industrial_spaces'),
    path('all-industrial-spaces/', IndustrialSpaceListView.as_view(), name='all_industrial_spaces'),
    path('edit-industrial-space/<int:pk>', IndustrialSpaceUpdateView.as_view(), name='edit_industrial_space'),
    path('delete-industrial-space/<int:pk>/', IndustrialSpaceDeleteView.as_view(), name='delete_industrial_space'),
    path('industrial-space-details/<int:pk>', IndustrialSpaceDetailView.as_view(), name='industrial_space_details'),

    path('add-residential-ensemble/', ResidentialEnsembleCreateView.as_view(), name='add_residential_ensemble'),
    path('residential-ensembles/', ResidentialEnsembleListView.as_view(), name='residential_ensembles_list'),
    path('edit-residential-ensemble/<int:pk>', ResidentialEnsembleUpdateView.as_view(), name='edit_residential_ensemble'),
    path('delete-residential-ensemble/<int:pk>/', ResidentialEnsembleDeleteView.as_view(), name='delete_residential_ensemble'),
    path('residential-ensemble-details/<int:pk>', ResidentialEnsembleDetailView.as_view(), name='residential_ensemble_details'),

    path('add-office-building/', OfficeBuildingCreateView.as_view(), name='add_office_building'),
    path('office-buildings/', OfficeBuildingListView.as_view(), name='office_buildings_list'),
    path('edit-office-building/<int:pk>', OfficeBuildingUpdateView.as_view(), name='edit_office_building'),
    path('delete-office-building/<int:pk>/', OfficeBuildingDeleteView.as_view(), name='delete_office_building'),
    path('office-building-details/<int:pk>', OfficeBuildingDetailView.as_view(), name='office_building_details'),

    path('property-added/', CreatePropertyDoneView.as_view(), name='property_added'),
    path('property-deleted/', DeletePropertyDoneView.as_view(), name='property_deleted'),

    path('add-new-property/', add_new_property, name='add_new_property'),
]
