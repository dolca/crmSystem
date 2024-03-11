from django.contrib import admin
from leads.models import ApartmentLead, HouseLead, TerrainLead, CommercialSpaceLead, OfficeSpaceLead, IndustrialSpaceLead

admin.site.register(ApartmentLead)
admin.site.register(HouseLead)
admin.site.register(TerrainLead)
admin.site.register(CommercialSpaceLead)
admin.site.register(OfficeSpaceLead)
admin.site.register(IndustrialSpaceLead)
