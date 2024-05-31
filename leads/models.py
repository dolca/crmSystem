from django.contrib.auth.models import User
from django.db.models import Model, SET_NULL, CharField, DecimalField, TextField, DateTimeField, DateField, TimeField, \
    IntegerField, BooleanField, ForeignKey
from contacts.models import Contact
from leads.selectors import STATUS, TIP_TRANZACTIE, MODALITATE_PLATA, URGENTA, ETICHETA, FINISAJE
from listings.models import Apartment, House, Terrain, CommercialSpace, OfficeSpace, IndustrialSpace
from listings.selectors import TIP_PROPRIETATE, TIP_APARTAMENT, DESTINATIE_AP, ETAJ_AP, STADIU_CONSTRUCTIE, MOBILIER, \
    CONFORT, COMPARTIMENTARE_AP, ORIENTARE, TIP_CASA, TIP_TEREN, DESTINATIE_TEREN, CLASIFICARE_TEREN, \
    UNITATE_SUPRAFATA, DESCHIDERE, TIP_IMOBIL_SPATIU, DESTINATIE_SP_COMERCIAL, TRAFIC_PIETONAL, ETAJ_SPATIU, \
    COMPARTIMENTARE_SPATIU, CLASA_SP_BIROURI, TIP_SP_INDUSTRIAL, DESTINATIE_SP_INDUSTRIAL, ETAJ_SP_INDUSTRIAL, JUDETE


class Lead(Model):
    lead_status = CharField(choices=STATUS, default='Activă', verbose_name='Status cerere')
    property_type = CharField(choices=TIP_PROPRIETATE, default='Apartament', verbose_name='Tip cerere')
    transaction_type = CharField(choices=TIP_TRANZACTIE, verbose_name='Tip tranzacție')

    contact = ForeignKey(Contact, on_delete=SET_NULL, null=True, verbose_name='Contact asociat')

    county = CharField(choices=JUDETE, verbose_name='Județ')
    city = CharField(max_length=30, verbose_name='Localitate')
    zone = CharField(max_length=30, null=True, blank=True, verbose_name='Zonă')
    street = CharField(max_length=40, null=True, blank=True, verbose_name='Stradă')

    budget = IntegerField(null=True, blank=True, verbose_name='Buget alocat')
    payment_method = CharField(choices=MODALITATE_PLATA, null=True, blank=True, verbose_name='Modalitate plată', )

    urgency = CharField(choices=URGENTA, default='Normal', verbose_name='Urgență')
    other_details = TextField(max_length=2000, null=True, blank=True, verbose_name='Alte detalii')

    labels = CharField(choices=ETICHETA, null=True, blank=True, verbose_name='Etichete')
    notes = TextField(max_length=2000, null=True, blank=True, verbose_name='Notițe proprii')

    deadline_date = DateField(null=True, blank=True, verbose_name='Data limită')
    deadline_time = TimeField(null=True, blank=True, verbose_name='Ora limită')

    created_at = DateTimeField(auto_now_add=True, verbose_name='Data introducerii')
    updated_at = DateTimeField(auto_now=True, verbose_name='Data ultimei actualizări')

    class Meta:
        abstract = True


class ApartmentLead(Lead):
    apartment_type = CharField(choices=TIP_APARTAMENT, verbose_name='Tip apartament')
    destination = CharField(choices=DESTINATIE_AP, verbose_name='Destinație')

    rooms_number = IntegerField(null=True, blank=True, verbose_name='Număr camere')
    nr_bedrooms = IntegerField(null=True, blank=True, verbose_name='Număr dormitoare')
    nr_bathrooms = IntegerField(null=True, blank=True, verbose_name='Număr băi')
    bathroom_window = BooleanField(default=False, verbose_name='Geam la baie')
    floor = CharField(choices=ETAJ_AP, null=True, blank=True, verbose_name='Etaj')
    excluded_ground_floor = BooleanField(default=False, verbose_name='Exclus parter')
    excluded_top_floor = BooleanField(default=False, verbose_name='Exclus ultimul etaj')
    nr_floors = IntegerField(null=True, blank=True, verbose_name='Număr etaje')

    minimal_surface = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață minimă (mp)')
    construction_status = CharField(choices=STADIU_CONSTRUCTIE, null=True, blank=True, verbose_name='Stadiu construcție')
    furniture = CharField(choices=MOBILIER, null=True, blank=True, verbose_name='Mobilier')
    comfort = CharField(choices=CONFORT, null=True, blank=True, verbose_name='Confort')
    ap_compart = CharField(choices=COMPARTIMENTARE_AP, null=True, blank=True, verbose_name='Compartimentare')
    orientation = CharField(choices=ORIENTARE, null=True, blank=True, verbose_name='Orientare')
    interior_finishes = CharField(choices=FINISAJE, null=True, blank=True, verbose_name='Stare interior')
    construction_year = IntegerField(null=True, blank=True, verbose_name='Anul construcției')

    basement = BooleanField(default=False, verbose_name='Subsol')
    semi_basement = BooleanField(default=False, verbose_name='Demisol')
    technical_floor = BooleanField(default=False, verbose_name='Etaj tehnic')
    loft = BooleanField(default=False, verbose_name='Mansardă')
    attic = BooleanField(default=False, verbose_name='Pod')
    elevator = BooleanField(default=False, verbose_name='Lift')

    created_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='created_apartment_leads',
                            verbose_name='Agent asociat')
    updated_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='updated_apartment_leads',
                            verbose_name='Actualizată de')
    assigned_listings = ForeignKey(Apartment, on_delete=SET_NULL, null=True, blank=True, verbose_name='Proprietăți asociate')

    def __str__(self):
        return f'{self.id}. {self.property_type} (Tip: {self.apartment_type}) - Contact: {self.contact} | Agent: {self.created_by}'


class HouseLead(Lead):
    house_type = CharField(choices=TIP_CASA, verbose_name='Tip casă')
    destination = CharField(choices=DESTINATIE_AP, null=True, blank=True, verbose_name='Destinație')

    rooms_number = IntegerField(null=True, blank=True, verbose_name='Număr camere')
    nr_bedrooms = IntegerField(null=True, blank=True, verbose_name='Număr dormitoare')
    nr_kitchens = IntegerField(null=True, blank=True, verbose_name='Număr bucătării')
    nr_bathrooms = IntegerField(null=True, blank=True, verbose_name='Număr băi')
    bathroom_window = BooleanField(default=False, verbose_name='Geam la baie')
    nr_floors = IntegerField(null=True, blank=True, verbose_name='Număr etaje')

    minimal_surface = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață minimă (mp)')
    terrain_surface = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Suprafață teren (mp)')
    construction_status = CharField(choices=STADIU_CONSTRUCTIE, null=True, blank=True, verbose_name='Stadiu construcție')
    furniture = CharField(choices=MOBILIER, null=True, blank=True, verbose_name='Mobilier')
    interior_finishes = CharField(choices=FINISAJE, null=True, blank=True, verbose_name='Stare interior')
    construction_year = IntegerField(null=True, blank=True, verbose_name='Anul construcției')

    basement = BooleanField(default=False, verbose_name='Subsol')
    semi_basement = BooleanField(default=False, verbose_name='Demisol')
    loft = BooleanField(default=False, verbose_name='Mansardă')
    attic = BooleanField(default=False, verbose_name='Pod')
    garage = BooleanField(default=False, verbose_name='Garaj')

    created_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='created_house_leads',
                            verbose_name='Agent asociat')
    updated_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='updated_house_leads',
                            verbose_name='Actualizată de')
    assigned_listings = ForeignKey(House, on_delete=SET_NULL, null=True, blank=True, verbose_name='Proprietăți asociate')

    def __str__(self):
        return f'{self.id}. {self.property_type} (Tip: {self.house_type}) - Contact: {self.contact} | Agent: {self.created_by}'


class TerrainLead(Lead):
    terrain_type = CharField(choices=TIP_TEREN, verbose_name='Tip teren')
    destination = CharField(choices=DESTINATIE_TEREN, verbose_name='Destinație')
    classification = CharField(choices=CLASIFICARE_TEREN, verbose_name='Clasificare')

    terrain_surface = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Suprafață teren')
    unit = CharField(choices=UNITATE_SUPRAFATA, null=True, blank=True, verbose_name='Unitate suprafață')
    street_front = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Front stradal (m)')
    opening_to = CharField(choices=DESCHIDERE, null=True, blank=True, verbose_name='Deschidere la')
    access_road_width = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Lățime drum acces (m)')

    pot = CharField(max_length=4, null=True, blank=True, verbose_name='POT (%)')
    cut = CharField(max_length=5, null=True, blank=True, verbose_name='CUT')
    urban_certificate = BooleanField(default=False, verbose_name='Certificat de urbanism')
    building_permit = BooleanField(default=False, verbose_name='Autorizație de construcție')
    pug = BooleanField(default=False, verbose_name='PUG aprobat')
    puz = BooleanField(default=False, verbose_name='PUZ aprobat')
    pud = BooleanField(default=False, verbose_name='PUD aprobat')

    created_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='created_terrain_leads',
                            verbose_name='Agent asociat')
    updated_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='updated_terrain_leads',
                            verbose_name='Actualizată de')
    assigned_listings = ForeignKey(Terrain, on_delete=SET_NULL, null=True, blank=True, verbose_name='Proprietăți asociate')

    def __str__(self):
        return f'{self.id}. {self.property_type} (Tip: {self.terrain_type}) - Contact: {self.contact} | Agent: {self.created_by}'


class CommercialSpaceLead(Lead):
    space_type = CharField(choices=TIP_IMOBIL_SPATIU, verbose_name='Tip imobil')
    destination = CharField(choices=DESTINATIE_SP_COMERCIAL, null=True, blank=True, verbose_name='Destinație')
    pedestrian_traffic = CharField(choices=TRAFIC_PIETONAL, null=True, blank=True, verbose_name='Trafic pietonal')

    rooms_number = IntegerField(null=True, blank=True, verbose_name='Număr camere')
    nr_locker_rooms = IntegerField(null=True, blank=True, verbose_name='Număr vestiare')
    nr_bathrooms = IntegerField(null=True, blank=True, verbose_name='Număr băi')
    floor = CharField(choices=ETAJ_SPATIU, null=True, blank=True, verbose_name='Etaj')
    nr_floors = IntegerField(null=True, blank=True, verbose_name='Număr etaje')

    minimal_surface = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață minimă (mp)')
    glass_case = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Vitrină (m)')
    inside_height = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Înălțime interioară (m)')
    space_compart = CharField(choices=COMPARTIMENTARE_SPATIU, null=True, blank=True, verbose_name='Compartimentare')
    nr_parking_spaces = IntegerField(null=True, blank=True, verbose_name='Număr locuri parcare')

    semi_basement = BooleanField(default=False, verbose_name='Demisol')
    technical_floor = BooleanField(default=False, verbose_name='Etaj tehnic')
    loft = BooleanField(default=False, verbose_name='Mansardă')

    created_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='created_commercial_space_leads',
                            verbose_name='Agent asociat')
    updated_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='updated_commercial_space_leads',
                            verbose_name='Actualizată de')
    assigned_listings = ForeignKey(CommercialSpace, on_delete=SET_NULL, null=True, blank=True, verbose_name='Proprietăți asociate')

    def __str__(self):
        return f'{self.id}. {self.property_type} (Tip: {self.space_type}) - Contact: {self.contact} | Agent: {self.created_by}'


class OfficeSpaceLead(Lead):
    space_type = CharField(choices=TIP_IMOBIL_SPATIU, verbose_name='Tip imobil')
    space_class = CharField(choices=CLASA_SP_BIROURI, null=True, blank=True, verbose_name='Clasă')

    rooms_number = IntegerField(null=True, blank=True, verbose_name='Număr camere')
    nr_bathrooms = IntegerField(null=True, blank=True, verbose_name='Număr băi')
    floor = CharField(choices=ETAJ_SPATIU, null=True, blank=True, verbose_name='Etaj')
    nr_floors = IntegerField(null=True, blank=True, verbose_name='Număr etaje')

    useful_surface = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Suprafață utilă (mp)')
    minimum_area = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Suprafață minimă (mp)')
    maximum_area = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață maximă (mp)')
    total_surface_offices = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Suprafață totală birouri (mp)')
    space_compart = CharField(choices=COMPARTIMENTARE_SPATIU, null=True, blank=True, verbose_name='Compartimentare')

    nr_underground_parking = IntegerField(null=True, blank=True, verbose_name='Nr. locuri parcare subterană')
    underground_parking_cost = IntegerField(null=True, blank=True, verbose_name='Cost loc parcare subterană')
    nr_surface_parking = IntegerField(null=True, blank=True, verbose_name='Nr. locuri parcare suprafață')
    surface_parking_cost = IntegerField(null=True, blank=True, verbose_name='Cost loc parcare suprafață')

    basement = BooleanField(default=False, verbose_name='Subsol')
    semi_basement = BooleanField(default=False, verbose_name='Demisol')
    technical_floor = BooleanField(default=False, verbose_name='Etaj tehnic')
    loft = BooleanField(default=False, verbose_name='Mansardă')
    elevator = BooleanField(default=False, verbose_name='Lift')

    created_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='created_office_space_leads',
                            verbose_name='Agent asociat')
    updated_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='updated_office_space_leads',
                            verbose_name='Actualizată de')
    assigned_listings = ForeignKey(OfficeSpace, on_delete=SET_NULL, null=True, blank=True, verbose_name='Proprietăți asociate')

    def __str__(self):
        return f'{self.id}. {self.property_type} (Tip: {self.space_type}) - Contact: {self.contact} | Agent: {self.created_by}'


class IndustrialSpaceLead(Lead):
    space_type = CharField(choices=TIP_SP_INDUSTRIAL, verbose_name='Tip spațiu')
    destination = CharField(choices=DESTINATIE_SP_INDUSTRIAL, null=True, blank=True, verbose_name='Destinație')

    rooms_number = IntegerField(null=True, blank=True, verbose_name='Număr camere')
    nr_locker_rooms = IntegerField(null=True, blank=True, verbose_name='Număr vestiare')
    nr_bathrooms = IntegerField(null=True, blank=True, verbose_name='Număr băi')
    floor = CharField(choices=ETAJ_SP_INDUSTRIAL, null=True, blank=True, verbose_name='Etaj')

    minimal_surface = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Suprafață minimă (mp)')
    space_compart = CharField(choices=COMPARTIMENTARE_SPATIU, null=True, blank=True, verbose_name='Compartimentare')
    terrain_surface = DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Suprafață teren (mp)')
    entrance_door_dimensions = CharField(max_length=15, null=True, blank=True, verbose_name='Dimensiuni uși intrare')
    inside_height = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Înălțime interioară (m)')

    powerline = BooleanField(default=False, verbose_name='Trifazic (380V)')
    truck_access = BooleanField(default=False, verbose_name='Acces camion')

    created_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='created_industrial_space_leads',
                            verbose_name='Agent asociat')
    updated_by = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='updated_industrial_space_leads',
                            verbose_name='Actualizată de')
    assigned_listings = ForeignKey(IndustrialSpace, on_delete=SET_NULL, null=True, blank=True, verbose_name='Proprietăți asociate')

    def __str__(self):
        return f'{self.id}. {self.property_type} (Tip: {self.space_type}) - Contact: {self.contact} | Agent: {self.created_by}'
