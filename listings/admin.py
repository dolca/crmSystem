from django.contrib import admin
from listings.models import ResidentialEnsemble, OfficeBuilding, Apartment, House, Terrain, CommercialSpace, \
    OfficeSpace, IndustrialSpace

admin.site.register(ResidentialEnsemble)
admin.site.register(OfficeBuilding)
admin.site.register(Apartment)
admin.site.register(House)
admin.site.register(Terrain)
admin.site.register(CommercialSpace)
admin.site.register(OfficeSpace)
admin.site.register(IndustrialSpace)
