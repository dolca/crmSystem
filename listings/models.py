from django.contrib.auth.models import User
from django.db.models import Model, SET_NULL, CASCADE, CharField, ForeignKey, TextField, IntegerField, ImageField, \
    DateTimeField, BooleanField, DecimalField
from contacts.models import Contact
from leads.selectors import MODALITATE_PLATA
from listings.selectors import STATUS_PROPRIETATE, TIP_PROPRIETATE, TIP_TRANZACTIE, DESTINATIE_AP, TIP_APARTAMENT, \
    COMPARTIMENTARE_AP, ORIENTARE, ETAJ_AP, CONFORT, FINISAJE, TIP_IMOBIL_AP, MATERIALE, STADIU_CONSTRUCTIE, TIP_CASA, \
    ACOPERIS, TIP_TEREN, UNITATE_SUPRAFATA, DESCHIDERE, CLASIFICARE_TEREN, DESTINATIE_TEREN, TIP_IMOBIL_SPATIU, \
    TRAFIC_PIETONAL, DESTINATIE_SP_COMERCIAL, ETAJ_SPATIU, COMPARTIMENTARE_SPATIU, CLASA_SP_BIROURI, \
    DESTINATIE_SP_INDUSTRIAL, TIP_SP_INDUSTRIAL, ETAJ_SP_INDUSTRIAL, TIP_IMOBIL_ANSAMBLU, DOTARI, IZOLATII_TERMICE, \
    DOTARI_IMOBIL, PARCARE, SISTEM_INCALZIRE, USA_INTRARE, USI_INTERIOR, MOBILIER, BUCATARIE, FERESTRE, ALTE_SPATII, \
    FACILITATI_TEREN, ALTE_FACILITATI, ELEMENTE_ECO, ALTE_FACILITATI_SP_COM, SERVICII_ASIGURATE, SIGURANTA_SECURITATE, \
    IT_C, SISTEM_ELECTRIC, ARHITECTURA, CLIMATIZARE_BIROU, FACILITATI_CLADIRE_PROXIMITATI, ALTE_FACILITATI_SP_IND, \
    TIP_PROPRIETAR, COTA_TVA, MONEDA, JUDETE


class Listing(Model):
    status = CharField(choices=STATUS_PROPRIETATE, default='Incompletă', verbose_name='Status proprietate⋆')
    property_type = CharField(choices=TIP_PROPRIETATE, default='apartment', verbose_name='Tip proprietate⋆')
    transaction_type = CharField(choices=TIP_TRANZACTIE, verbose_name='Tip tranzacție⋆')

    contact = ForeignKey(Contact, on_delete=SET_NULL, null=True, verbose_name='Contact asociat')

    title = CharField(max_length=70, null=True, blank=True, verbose_name='Titlu')
    description = TextField(max_length=2000, null=True, blank=True, verbose_name='Descriere')
    county = CharField(choices=JUDETE, verbose_name='Județ⋆')
    city = CharField(max_length=30, verbose_name='Localitate⋆')
    zone = CharField(max_length=20, verbose_name='Zonă⋆')
    street_address = CharField(max_length=40, verbose_name='Stradă⋆')
    street_nr = IntegerField(verbose_name='Număr stradă⋆')

    images = ImageField(upload_to='static/images/listings/', null=True, blank=True, verbose_name='Imagini')

    payment_method = CharField(choices=MODALITATE_PLATA, null=True, blank=True, verbose_name='Modalitate plată acceptată', )
    other_details = TextField(max_length=2000, null=True, blank=True, verbose_name='Alte detalii')

    created_at = DateTimeField(auto_now_add=True, verbose_name='Data adăugării')
    updated_at = DateTimeField(auto_now=True, verbose_name='Data ultimei actualizări')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.title}'


class ResidentialEnsemble(Model):
    status = CharField(choices=STATUS_PROPRIETATE, default='Incompletă', verbose_name='Status proprietate⋆')

    contact = ForeignKey(Contact, on_delete=SET_NULL, null=True, blank=True, verbose_name='Contact asociat')

    title = CharField(max_length=70, null=True, blank=True, verbose_name='Titlu')
    description = TextField(max_length=2000, null=True, blank=True, verbose_name='Descriere')
    county = CharField(choices=JUDETE, verbose_name='Județ⋆')
    city = CharField(max_length=30, verbose_name='Localitate⋆')
    zone = CharField(max_length=20, verbose_name='Zonă⋆')
    street_address = CharField(max_length=40, verbose_name='Stradă⋆')
    street_nr = IntegerField(verbose_name='Număr stradă⋆')

    building_type = CharField(choices=TIP_IMOBIL_ANSAMBLU, verbose_name='Tip imobil⋆')
    construction_year = IntegerField(verbose_name='Anul construcției⋆')
    construction_status = CharField(choices=STADIU_CONSTRUCTIE, verbose_name='Stadiu construcție⋆')
    construction_materials = CharField(choices=MATERIALE, null=True, blank=True, verbose_name='Materiale construcție')
    interior_finishes = CharField(choices=FINISAJE, verbose_name='Stare interior⋆')
    nr_floors = IntegerField(verbose_name='Număr etaje⋆')
    semi_basement = BooleanField(default=False, verbose_name='Demisol')
    technical_floor = BooleanField(default=False, verbose_name='Etaj tehnic')
    loft = BooleanField(default=False, verbose_name='Mansardă')
    attic = BooleanField(default=False, verbose_name='Pod')

    underground_parking = BooleanField(default=False, verbose_name='Parcare subterană')
    nr_underground_parking = IntegerField(null=True, blank=True, verbose_name='Nr. locuri parcare subterană')
    underground_parking_cost = IntegerField(null=True, blank=True, verbose_name='Cost loc parcare subterană')
    surface_parking = BooleanField(default=False, verbose_name='Parcare suprafață')
    nr_surface_parking = IntegerField(null=True, blank=True, verbose_name='Nr. locuri parcare suprafață')
    surface_parking_cost = IntegerField(null=True, blank=True, verbose_name='Cost loc parcare suprafață')

    finishes = TextField(max_length=2000, null=True, blank=True, verbose_name='Finisaje imobil')
    technical_details = TextField(max_length=2000, null=True, blank=True, verbose_name='Detalii tehnice')

    thermal_insulation = CharField(choices=IZOLATII_TERMICE, null=True, blank=True, verbose_name='Izolație termică')
    other_spaces = CharField(choices=ALTE_SPATII, null=True, blank=True, verbose_name='Alte spații')

    other_details = TextField(max_length=2000, null=True, blank=True, verbose_name='Alte detalii')

    images = ImageField(upload_to='static/images/listings/', null=True, blank=True, verbose_name='Imagini')

    created_at = DateTimeField(auto_now_add=True, verbose_name='Data adăugării')
    updated_at = DateTimeField(auto_now=True, verbose_name='Data ultimei actualizări')

    def __str__(self):
        return f'{self.title}'


class OfficeBuilding(Model):
    status = CharField(choices=STATUS_PROPRIETATE, default='Incompletă', verbose_name='Status proprietate⋆')

    contact = ForeignKey(Contact, on_delete=SET_NULL, null=True, blank=True, verbose_name='Contact asociat')

    title = CharField(max_length=70, null=True, blank=True, verbose_name='Titlu')
    description = TextField(max_length=2000, null=True, blank=True, verbose_name='Descriere')
    county = CharField(choices=JUDETE, verbose_name='Județ⋆')
    city = CharField(max_length=30, verbose_name='Localitate⋆')
    zone = CharField(max_length=20, verbose_name='Zonă⋆')
    street_address = CharField(max_length=40, verbose_name='Stradă⋆')
    street_nr = IntegerField(verbose_name='Număr stradă⋆')

    construction_year = IntegerField(verbose_name='Anul construcției⋆')
    construction_status = CharField(choices=STADIU_CONSTRUCTIE, verbose_name='Stadiu construcție⋆')
    construction_materials = CharField(choices=MATERIALE, null=True, blank=True, verbose_name='Materiale construcție')
    interior_finishes = CharField(choices=FINISAJE, verbose_name='Stare interior⋆')
    nr_floors = IntegerField(verbose_name='Număr etaje⋆')
    space_class = CharField(choices=CLASA_SP_BIROURI, null=True, blank=True, verbose_name='Clasă')
    minimum_area = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Suprafață minimă (mp)')
    maximum_area = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață maximă (mp)')
    total_surface_offices = DecimalField(max_digits=6, decimal_places=2, verbose_name='Suprafață totală birouri (mp)⋆')
    common_area_factor = IntegerField(null=True, blank=True, verbose_name='Factor suprafețe comune (%)')
    occupancy_rate = IntegerField(null=True, blank=True, verbose_name='Rata de ocupare (%)')

    underground_parking = BooleanField(default=False, verbose_name='Parcare subterană')
    nr_underground_parking = IntegerField(null=True, blank=True, verbose_name='Nr. locuri parcare subterană')
    underground_parking_cost = IntegerField(null=True, blank=True, verbose_name='Cost loc parcare subterană')
    surface_parking = BooleanField(default=False, verbose_name='Parcare suprafață')
    nr_surface_parking = IntegerField(null=True, blank=True, verbose_name='Nr. locuri parcare suprafață')
    surface_parking_cost = IntegerField(null=True, blank=True, verbose_name='Cost loc parcare suprafață')

    nr_elevators = IntegerField(null=True, blank=True, verbose_name='Număr lifturi')
    semi_basement = BooleanField(default=False, verbose_name='Demisol')
    mezzanine = BooleanField(default=False, verbose_name='Mezanin')
    technical_floor = BooleanField(default=False, verbose_name='Etaj tehnic')
    loft = BooleanField(default=False, verbose_name='Mansardă')

    finishes = TextField(max_length=2000, null=True, blank=True, verbose_name='Finisaje imobil')
    technical_details = TextField(max_length=2000, null=True, blank=True, verbose_name='Detalii tehnice')

    services_provided = CharField(choices=SERVICII_ASIGURATE, null=True, blank=True, verbose_name='Servicii asigurate')
    safety_security = CharField(choices=SIGURANTA_SECURITATE, null=True, blank=True, verbose_name='Siguranță și securitate')
    it_c = CharField(choices=IT_C, null=True, blank=True, verbose_name='IT & C')
    electrical_system = CharField(choices=SISTEM_ELECTRIC, null=True, blank=True, verbose_name='Sistem electric')
    eco_elements = CharField(choices=ELEMENTE_ECO, null=True, blank=True, verbose_name='Elemente ECO')
    architecture = CharField(choices=ARHITECTURA, null=True, blank=True, verbose_name='Arhitectură')
    air_conditioning = CharField(choices=CLIMATIZARE_BIROU, null=True, blank=True, verbose_name='Climatizare birou')
    building_facilities_proximity = CharField(choices=FACILITATI_CLADIRE_PROXIMITATI, null=True, blank=True,
                                              verbose_name='Facilități clădire / proximități')

    other_details = TextField(max_length=2000, null=True, blank=True, verbose_name='Alte detalii')

    images = ImageField(upload_to='static/images/listings/', null=True, blank=True, verbose_name='Imagini')

    created_at = DateTimeField(auto_now_add=True, verbose_name='Data adăugării')
    updated_at = DateTimeField(auto_now=True, verbose_name='Data ultimei actualizări')

    def __str__(self):
        return f'{self.title}'


class Apartment(Listing):
    residential_ensemble = ForeignKey(ResidentialEnsemble, on_delete=CASCADE, null=True, blank=True, verbose_name='Ansamblu rezidențial')
    block = CharField(max_length=4, null=True, blank=True, verbose_name='Bloc')
    scale = CharField(max_length=3, null=True, blank=True, verbose_name='Scară')
    apartment_nr = IntegerField(verbose_name='Număr apartament⋆')

    apartment_type = CharField(choices=TIP_APARTAMENT, verbose_name='Tip apartament⋆')
    destination = CharField(choices=DESTINATIE_AP, null=True, blank=True, verbose_name='Destinație')
    ap_compart = CharField(choices=COMPARTIMENTARE_AP, verbose_name='Compartimentare⋆')
    orientation = CharField(choices=ORIENTARE, null=True, blank=True, verbose_name='Orientare')
    floor = CharField(choices=ETAJ_AP, verbose_name='Etaj⋆')
    comfort = CharField(choices=CONFORT, null=True, blank=True, verbose_name='Confort')
    interior_finishes = CharField(choices=FINISAJE, verbose_name='Stare interior⋆')
    useful_surface = DecimalField(max_digits=5, decimal_places=2, verbose_name='Suprafață utilă (mp)⋆')
    total_surface = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață totală (mp)')
    balcony_surface = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Suprafață balcoane (mp)')
    terrace_surface = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață terasă (mp)')

    rooms_number = IntegerField(verbose_name='Număr camere⋆')
    nr_bedrooms = IntegerField(null=True, blank=True, verbose_name='Număr dormitoare')
    nr_bathrooms = IntegerField(null=True, blank=True, verbose_name='Număr băi')
    bathroom_window = BooleanField(default=False, verbose_name='Geam la baie')
    nr_balconies = IntegerField(null=True, blank=True, verbose_name='Număr balcoane')
    nr_terraces = IntegerField(null=True, blank=True, verbose_name='Număr terase')
    garage = BooleanField(default=False, verbose_name='Garaj')
    nr_parking_spaces = IntegerField(null=True, blank=True, verbose_name='Număr locuri parcare')

    building_type = CharField(choices=TIP_IMOBIL_AP, null=True, blank=True, verbose_name='Tip imobil')
    construction_year = IntegerField(verbose_name='Anul construcției⋆')
    construction_materials = CharField(choices=MATERIALE, null=True, blank=True, verbose_name='Materiale construcție')
    construction_status = CharField(choices=STADIU_CONSTRUCTIE, null=True, blank=True, verbose_name='Stadiu construcție')
    nr_floors = IntegerField(verbose_name='Număr etaje⋆')
    semi_basement = BooleanField(default=False, verbose_name='Demisol')
    technical_floor = BooleanField(default=False, verbose_name='Etaj tehnic')
    loft = BooleanField(default=False, verbose_name='Mansardă')
    attic = BooleanField(default=False, verbose_name='Pod')

    facilities = CharField(choices=DOTARI, null=True, blank=True, verbose_name='Dotări')
    thermal_insulation = CharField(choices=IZOLATII_TERMICE, null=True, blank=True, verbose_name='Izolație termică')
    building_facilities = CharField(choices=DOTARI_IMOBIL, null=True, blank=True, verbose_name='Dotări imobil')
    parking = CharField(choices=PARCARE, null=True, blank=True, verbose_name='Parcare')
    heating_system = CharField(choices=SISTEM_INCALZIRE, null=True, blank=True, verbose_name='Sistem încălzire')
    entrance_door = CharField(choices=USA_INTRARE, null=True, blank=True, verbose_name='Ușă intrare')
    interior_doors = CharField(choices=USI_INTERIOR, null=True, blank=True, verbose_name='Uși interior')
    furniture = CharField(choices=MOBILIER, null=True, blank=True, verbose_name='Mobilier')
    kitchen = CharField(choices=BUCATARIE, null=True, blank=True, verbose_name='Bucătărie')
    windows = CharField(choices=FERESTRE, null=True, blank=True, verbose_name='Ferestre')
    other_spaces = CharField(choices=ALTE_SPATII, null=True, blank=True, verbose_name='Alte spații')

    price = DecimalField(max_digits=9, decimal_places=2, verbose_name='Preț tranzacționare⋆')
    last_price = DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, verbose_name='Ultimul preț în mână')
    negotiable = BooleanField(default=False, verbose_name='Negociabil')
    price_per_sqm = DecimalField(max_digits=7, decimal_places=2, editable=False, verbose_name='Preț / mp')
    owner_type = CharField(choices=TIP_PROPRIETAR, null=True, blank=True, verbose_name='Tip proprietar')
    VAT_rate = CharField(choices=COTA_TVA, default='Nu se aplică TVA', null=True, blank=True, verbose_name='TVA')
    currency = CharField(choices=MONEDA, default='euro', null=True, blank=True, verbose_name='Monedă')
    percentage_commission = IntegerField(null=True, blank=True, verbose_name='Comision de la proprietar (%)')
    fixed_commission = IntegerField(null=True, blank=True, verbose_name='Comision fix de la proprietar')
    exclusive_representation = BooleanField(default=False, verbose_name='Reprezentare exclusivă')

    assigned_user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='my_apartment_list', verbose_name='Agent asociat')


class House(Listing):
    residential_ensemble = ForeignKey(ResidentialEnsemble, on_delete=CASCADE, null=True, blank=True, verbose_name='Ansamblu rezidențial')

    house_type = CharField(choices=TIP_CASA, verbose_name='Tip casă⋆')
    destination = CharField(choices=DESTINATIE_AP, null=True, blank=True, verbose_name='Destinație')
    interior_finishes = CharField(choices=FINISAJE, verbose_name='Stare interior⋆')
    useful_surface = DecimalField(max_digits=5, decimal_places=2, verbose_name='Suprafață utilă (mp)⋆')
    built_area = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață construită (mp)')
    terrain_surface = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Suprafață utilă teren (mp)')
    terrain_total_surface = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Suprafață totală teren (mp)')
    terrace_surface = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață terasă (mp)')
    balcony_surface = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Suprafață balcoane (mp)')
    opening = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Deschidere (m)')

    roof = CharField(choices=ACOPERIS, null=True, blank=True, verbose_name='Acoperiș')
    construction_status = CharField(choices=STADIU_CONSTRUCTIE, null=True, blank=True, verbose_name='Stadiu construcție')
    construction_year = IntegerField(verbose_name='Anul construcției⋆')
    construction_materials = CharField(choices=MATERIALE, null=True, blank=True, verbose_name='Materiale construcție')
    nr_floors = IntegerField(null=True, blank=True, verbose_name='Număr etaje')
    semi_basement = BooleanField(default=False, verbose_name='Demisol')
    technical_floor = BooleanField(default=False, verbose_name='Etaj tehnic')
    loft = BooleanField(default=False, verbose_name='Mansardă')
    attic = BooleanField(default=False, verbose_name='Pod')

    rooms_number = IntegerField(verbose_name='Număr camere⋆')
    nr_bedrooms = IntegerField(null=True, blank=True, verbose_name='Număr dormitoare')
    nr_kitchens = IntegerField(null=True, blank=True, verbose_name='Număr bucătării')
    nr_bathrooms = IntegerField(null=True, blank=True, verbose_name='Număr băi')
    bathroom_window = BooleanField(default=False, verbose_name='Geam la baie')
    nr_terraces = IntegerField(null=True, blank=True, verbose_name='Număr terase')
    nr_balconies = IntegerField(null=True, blank=True, verbose_name='Număr balcoane')
    garage = BooleanField(default=False, verbose_name='Garaj')
    nr_parking_spaces = IntegerField(null=True, blank=True, verbose_name='Număr locuri parcare')

    facilities = CharField(choices=DOTARI, null=True, blank=True, verbose_name='Dotări')
    thermal_insulation = CharField(choices=IZOLATII_TERMICE, null=True, blank=True, verbose_name='Izolație termică')
    building_facilities = CharField(choices=DOTARI_IMOBIL, null=True, blank=True, verbose_name='Dotări imobil')
    parking = CharField(choices=PARCARE, null=True, blank=True, verbose_name='Parcare')
    heating_system = CharField(choices=SISTEM_INCALZIRE, null=True, blank=True, verbose_name='Sistem încălzire')
    entrance_door = CharField(choices=USA_INTRARE, null=True, blank=True, verbose_name='Ușă intrare')
    interior_doors = CharField(choices=USI_INTERIOR, null=True, blank=True, verbose_name='Uși interior')
    furniture = CharField(choices=MOBILIER, null=True, blank=True, verbose_name='Mobilier')
    kitchen = CharField(choices=BUCATARIE, null=True, blank=True, verbose_name='Bucătărie')
    windows = CharField(choices=FERESTRE, null=True, blank=True, verbose_name='Ferestre')
    other_spaces = CharField(choices=ALTE_SPATII, null=True, blank=True, verbose_name='Alte spații')

    price = DecimalField(max_digits=9, decimal_places=2, verbose_name='Preț tranzacționare⋆')
    last_price = DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, verbose_name='Ultimul preț în mână')
    negotiable = BooleanField(default=False, verbose_name='Negociabil')
    price_per_sqm = DecimalField(max_digits=7, decimal_places=2, editable=False, verbose_name='Preț / mp')
    owner_type = CharField(choices=TIP_PROPRIETAR, null=True, blank=True, verbose_name='Tip proprietar')
    VAT_rate = CharField(choices=COTA_TVA, default='Nu se aplică TVA', null=True, blank=True, verbose_name='TVA')
    currency = CharField(choices=MONEDA, default='euro', null=True, blank=True, verbose_name='Monedă')
    percentage_commission = IntegerField(null=True, blank=True, verbose_name='Comision de la proprietar (%)')
    fixed_commission = IntegerField(null=True, blank=True, verbose_name='Comision fix de la proprietar')
    exclusive_representation = BooleanField(default=False, verbose_name='Reprezentare exclusivă')

    assigned_user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='my_house_list', verbose_name='Agent asociat')


class Terrain(Listing):
    terrain_type = CharField(choices=TIP_TEREN, verbose_name='Tip teren⋆')
    destination = CharField(choices=DESTINATIE_TEREN, null=True, blank=True, verbose_name='Destinație')
    classification = CharField(choices=CLASIFICARE_TEREN, verbose_name='Clasificare⋆')
    terrain_surface = DecimalField(max_digits=6, decimal_places=2, verbose_name='Suprafață teren⋆')
    unit = CharField(choices=UNITATE_SUPRAFATA, verbose_name='Unitate suprafață⋆')
    street_front = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Front stradal (m)')
    nr_street_fronts = IntegerField(null=True, blank=True, verbose_name='Număr fronturi stradale')
    opening_to = CharField(choices=DESCHIDERE, null=True, blank=True, verbose_name='Deschidere la')
    fusion_degree = IntegerField(null=True, blank=True, verbose_name='Grad de comasare (%)')
    inclination = IntegerField(null=True, blank=True, verbose_name='Înclinație (°)')
    incidence_value = IntegerField(null=True, blank=True, verbose_name='Valoare incidență')
    construction = BooleanField(default=False, verbose_name='Construcție pe teren')
    construction_surface = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață construcție (mp)')
    access_road_width = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Lățime drum acces (m)')

    pot = CharField(max_length=4, null=True, blank=True, verbose_name='POT (%)')
    cut = CharField(max_length=5, null=True, blank=True, verbose_name='CUT')
    building_permit = BooleanField(default=False, verbose_name='Autorizație de construcție')
    pug = BooleanField(default=False, verbose_name='PUG')
    puz = BooleanField(default=False, verbose_name='PUZ')
    pud = BooleanField(default=False, verbose_name='PUD')
    urban_certificate = BooleanField(default=False, verbose_name='Certificat de urbanism')
    maximum_nr_levels = IntegerField(null=True, blank=True, verbose_name='Număr maxim niveluri')

    land_facilities = CharField(choices=FACILITATI_TEREN, null=True, blank=True, verbose_name='Facilități teren')
    other_features = CharField(choices=ALTE_FACILITATI, null=True, blank=True, verbose_name='Alte facilități')

    price = DecimalField(max_digits=9, decimal_places=2, verbose_name='Preț tranzacționare⋆')
    last_price = DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, verbose_name='Ultimul preț în mână')
    negotiable = BooleanField(default=False, verbose_name='Negociabil')
    price_per_sqm = DecimalField(max_digits=7, decimal_places=2, editable=False, verbose_name='Preț / mp')
    owner_type = CharField(choices=TIP_PROPRIETAR, null=True, blank=True, verbose_name='Tip proprietar')
    VAT_rate = CharField(choices=COTA_TVA, default='Nu se aplică TVA', null=True, blank=True, verbose_name='TVA')
    currency = CharField(choices=MONEDA, default='euro', null=True, blank=True, verbose_name='Monedă')
    percentage_commission = IntegerField(null=True, blank=True, verbose_name='Comision de la proprietar (%)')
    fixed_commission = IntegerField(null=True, blank=True, verbose_name='Comision fix de la proprietar')
    exclusive_representation = BooleanField(default=False, verbose_name='Reprezentare exclusivă')

    assigned_user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='my_terrain_list', verbose_name='Agent asociat')


class CommercialSpace(Listing):
    residential_ensemble = ForeignKey(ResidentialEnsemble, on_delete=CASCADE, null=True, blank=True, verbose_name='Ansamblu rezidențial')
    office_building = ForeignKey(OfficeBuilding, on_delete=CASCADE, null=True, blank=True, verbose_name='Clădire de birouri')
    block = CharField(max_length=4, null=True, blank=True, verbose_name='Bloc')
    space_nr = IntegerField(verbose_name='Număr spațiu⋆')

    space_type = CharField(choices=TIP_IMOBIL_SPATIU, verbose_name='Tip imobil⋆')
    destination = CharField(choices=DESTINATIE_SP_COMERCIAL, null=True, blank=True, verbose_name='Destinație')
    pedestrian_traffic = CharField(choices=TRAFIC_PIETONAL, null=True, blank=True, verbose_name='Trafic pietonal')
    floor = CharField(choices=ETAJ_SPATIU, verbose_name='Etaj⋆')
    rooms_number = IntegerField(null=True, blank=True, verbose_name='Număr camere')
    nr_locker_rooms = IntegerField(null=True, blank=True, verbose_name='Număr vestiare')
    nr_bathrooms = IntegerField(null=True, blank=True, verbose_name='Număr băi')
    nr_kitchens = IntegerField(null=True, blank=True, verbose_name='Număr bucătării')
    nr_terraces = IntegerField(null=True, blank=True, verbose_name='Număr terase')
    useful_surface = DecimalField(max_digits=5, decimal_places=2, verbose_name='Suprafață utilă (mp)⋆')
    total_surface = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață totală (mp)')
    street_front = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Front stradal (m)')
    glass_case = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Vitrină (m)')
    inside_height = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Înălțime interioară (m)')
    space_compart = CharField(choices=COMPARTIMENTARE_SPATIU, null=True, blank=True, verbose_name='Compartimentare')
    nr_parking_spaces = IntegerField(null=True, blank=True, verbose_name='Număr locuri parcare')

    construction_year = IntegerField(verbose_name='Anul construcției⋆')
    nr_floors = IntegerField(verbose_name='Număr etaje⋆')
    semi_basement = BooleanField(default=False, verbose_name='Demisol')
    technical_floor = BooleanField(default=False, verbose_name='Etaj tehnic')
    loft = BooleanField(default=False, verbose_name='Mansardă')

    land_facilities = CharField(choices=FACILITATI_TEREN, null=True, blank=True, verbose_name='Facilități teren')
    eco_elements = CharField(choices=ELEMENTE_ECO, null=True, blank=True, verbose_name='Elemente ECO')
    parking = CharField(choices=PARCARE, null=True, blank=True, verbose_name='Parcare')
    other_facilities_com_sp = CharField(choices=ALTE_FACILITATI_SP_COM, null=True, blank=True, verbose_name='Alte facilități')

    price = DecimalField(max_digits=9, decimal_places=2, verbose_name='Preț tranzacționare⋆')
    last_price = DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, verbose_name='Ultimul preț în mână')
    negotiable = BooleanField(default=False, verbose_name='Negociabil')
    price_per_sqm = DecimalField(max_digits=7, decimal_places=2, editable=False, verbose_name='Preț / mp')
    owner_type = CharField(choices=TIP_PROPRIETAR, null=True, blank=True, verbose_name='Tip proprietar')
    VAT_rate = CharField(choices=COTA_TVA, default='Nu se aplică TVA', null=True, blank=True, verbose_name='TVA')
    currency = CharField(choices=MONEDA, default='euro', null=True, blank=True, verbose_name='Monedă')
    percentage_commission = IntegerField(null=True, blank=True, verbose_name='Comision de la proprietar (%)')
    fixed_commission = IntegerField(null=True, blank=True, verbose_name='Comision fix de la proprietar')
    exclusive_representation = BooleanField(default=False, verbose_name='Reprezentare exclusivă')

    assigned_user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='my_commercial_space_list', verbose_name='Agent asociat')


class OfficeSpace(Listing):
    office_building = ForeignKey(OfficeBuilding, on_delete=CASCADE, null=True, blank=True, verbose_name='Clădire de birouri')
    space_nr = IntegerField(verbose_name='Număr spațiu⋆')

    space_type = CharField(choices=TIP_IMOBIL_SPATIU, verbose_name='Tip imobil⋆')
    floor = CharField(choices=ETAJ_SPATIU, verbose_name='Etaj⋆')
    space_class = CharField(choices=CLASA_SP_BIROURI, null=True, blank=True, verbose_name='Clasă')
    rooms_number = IntegerField(null=True, blank=True, verbose_name='Număr camere')
    nr_bathrooms = IntegerField(null=True, blank=True, verbose_name='Număr băi')
    useful_surface = DecimalField(max_digits=6, decimal_places=2, verbose_name='Suprafață utilă (mp)⋆')
    total_surface = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Suprafață totală (mp)')
    nr_terraces = IntegerField(null=True, blank=True, verbose_name='Număr terase')

    minimum_area = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Suprafață minimă (mp)')
    maximum_area = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Suprafață maximă (mp)')
    total_surface_offices = DecimalField(max_digits=6, decimal_places=2, verbose_name='Suprafață totală birouri (mp)⋆')
    common_area_factor = IntegerField(null=True, blank=True, verbose_name='Factor suprafețe comune (%)')
    occupancy_rate = IntegerField(null=True, blank=True, verbose_name='Rata de ocupare (%)')
    space_compart = CharField(choices=COMPARTIMENTARE_SPATIU, null=True, blank=True, verbose_name='Compartimentare')

    underground_parking = BooleanField(default=False, verbose_name='Parcare subterană')
    underground_parking_available = IntegerField(null=True, blank=True, verbose_name='Parcări subterane disponibile')
    underground_parking_cost = IntegerField(null=True, blank=True, verbose_name='Cost loc parcare subterană')
    surface_parking = BooleanField(default=False, verbose_name='Parcare suprafață')
    surface_parking_available = IntegerField(null=True, blank=True, verbose_name='Parcări suprafață disponibile')
    surface_parking_cost = IntegerField(null=True, blank=True, verbose_name='Cost loc parcare suprafață')

    construction_year = IntegerField(verbose_name='Anul construcției⋆')
    nr_floors = IntegerField(verbose_name='Număr etaje⋆')
    nr_elevators = IntegerField(null=True, blank=True, verbose_name='Număr lifturi')
    semi_basement = BooleanField(default=False, verbose_name='Demisol')
    technical_floor = BooleanField(default=False, verbose_name='Etaj tehnic')
    loft = BooleanField(default=False, verbose_name='Mansardă')

    services_provided = CharField(choices=SERVICII_ASIGURATE, null=True, blank=True, verbose_name='Servicii asigurate')
    safety_security = CharField(choices=SIGURANTA_SECURITATE, null=True, blank=True, verbose_name='Siguranță și securitate')
    it_c = CharField(choices=IT_C, null=True, blank=True, verbose_name='IT & C')
    electrical_system = CharField(choices=SISTEM_ELECTRIC, null=True, blank=True, verbose_name='Sistem electric')
    eco_elements = CharField(choices=ELEMENTE_ECO, null=True, blank=True, verbose_name='Elemente ECO')
    architecture = CharField(choices=ARHITECTURA, null=True, blank=True, verbose_name='Arhitectură')
    air_conditioning = CharField(choices=CLIMATIZARE_BIROU, null=True, blank=True, verbose_name='Climatizare birou')
    building_facilities_proximity = CharField(choices=FACILITATI_CLADIRE_PROXIMITATI, null=True, blank=True,
                                              verbose_name='Facilități clădire / proximități')
    parking = CharField(choices=PARCARE, null=True, blank=True, verbose_name='Parcare')

    price = DecimalField(max_digits=9, decimal_places=2, verbose_name='Preț tranzacționare⋆')
    last_price = DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, verbose_name='Ultimul preț în mână')
    negotiable = BooleanField(default=False, verbose_name='Negociabil')
    price_per_sqm = DecimalField(max_digits=7, decimal_places=2, editable=False, verbose_name='Preț / mp')
    owner_type = CharField(choices=TIP_PROPRIETAR, null=True, blank=True, verbose_name='Tip proprietar')
    VAT_rate = CharField(choices=COTA_TVA, default='Nu se aplică TVA', null=True, blank=True, verbose_name='TVA')
    currency = CharField(choices=MONEDA, default='euro', null=True, blank=True, verbose_name='Monedă')
    percentage_commission = IntegerField(null=True, blank=True, verbose_name='Comision de la proprietar (%)')
    fixed_commission = IntegerField(null=True, blank=True, verbose_name='Comision fix de la proprietar')
    exclusive_representation = BooleanField(default=False, verbose_name='Reprezentare exclusivă')

    assigned_user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='my_office_space_list', verbose_name='Agent asociat')


class IndustrialSpace(Listing):
    space_type = CharField(choices=TIP_SP_INDUSTRIAL, verbose_name='Tip spațiu⋆')
    destination = CharField(choices=DESTINATIE_SP_INDUSTRIAL, null=True, blank=True, verbose_name='Destinație')
    floor = CharField(choices=ETAJ_SP_INDUSTRIAL, null=True, blank=True, verbose_name='Etaj')
    space_class = CharField(choices=CLASA_SP_BIROURI, null=True, blank=True, verbose_name='Clasă birouri')
    rooms_number = IntegerField(null=True, blank=True, verbose_name='Număr camere')
    nr_locker_rooms = IntegerField(null=True, blank=True, verbose_name='Număr vestiare')
    nr_bathrooms = IntegerField(null=True, blank=True, verbose_name='Număr băi')
    nr_kitchens = IntegerField(null=True, blank=True, verbose_name='Număr bucătării')
    nr_terraces = IntegerField(null=True, blank=True, verbose_name='Număr terase')

    useful_surface = DecimalField(max_digits=7, decimal_places=2, verbose_name='Suprafață utilă (mp)⋆')
    built_area = DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Suprafață construită (mp)')
    total_surface_offices = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Suprafață totală birouri (mp)')
    space_compart = CharField(choices=COMPARTIMENTARE_SPATIU, null=True, blank=True, verbose_name='Compartimentare')
    glass_case = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Vitrină (m)')
    construction_year = IntegerField(verbose_name='Anul construcției⋆')
    terrain_surface = DecimalField(max_digits=7, decimal_places=2, verbose_name='Suprafață teren (mp)⋆')
    production_area = DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Suprafață producție (mp)')
    storage_area = DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Suprafață depozitare (mp)')
    entrance_door_dimensions = CharField(max_length=15, null=True, blank=True, verbose_name='Dimensiuni uși intrare')
    inside_height = DecimalField(max_digits=4, decimal_places=2, verbose_name='Înălțime interioară (m)⋆')
    nr_parking_spaces = IntegerField(null=True, blank=True, verbose_name='Număr locuri parcare')

    land_facilities = CharField(choices=FACILITATI_TEREN, null=True, blank=True, verbose_name='Facilități teren')
    parking = CharField(choices=PARCARE, null=True, blank=True, verbose_name='Parcare')
    other_facilities_ind_sp = CharField(choices=ALTE_FACILITATI_SP_IND, null=True, blank=True,
                                        verbose_name='Alte facilități spațiu industrial')

    price = DecimalField(max_digits=9, decimal_places=2, verbose_name='Preț tranzacționare⋆')
    last_price = DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, verbose_name='Ultimul preț în mână')
    negotiable = BooleanField(default=False, verbose_name='Negociabil')
    price_per_sqm = DecimalField(max_digits=7, decimal_places=2, editable=False, verbose_name='Preț / mp')
    owner_type = CharField(choices=TIP_PROPRIETAR, null=True, blank=True, verbose_name='Tip proprietar')
    VAT_rate = CharField(choices=COTA_TVA, default='Nu se aplică TVA', null=True, blank=True, verbose_name='TVA')
    currency = CharField(choices=MONEDA, default='euro', null=True, blank=True, verbose_name='Monedă')
    percentage_commission = IntegerField(null=True, blank=True, verbose_name='Comision de la proprietar (%)')
    fixed_commission = IntegerField(null=True, blank=True, verbose_name='Comision fix de la proprietar')
    exclusive_representation = BooleanField(default=False, verbose_name='Reprezentare exclusivă')

    assigned_user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='my_industrial_space_list', verbose_name='Agent asociat')
