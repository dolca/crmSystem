from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.forms import ModelForm, Select, TextInput, Textarea, EmailInput, NumberInput, DateInput, SelectMultiple, \
    CheckboxInput, ModelChoiceField, HiddenInput
from multiupload.fields import MultiImageField
from contacts.models import Contact
from listings.models import Listing, ResidentialEnsemble, OfficeBuilding, Apartment, House, Terrain, CommercialSpace, \
    OfficeSpace, IndustrialSpace


########################################################################################################################
#                               ---   FORMULARE CREARE   ---

class ListingCreateForm(ModelForm):
    images = MultiImageField(required=False)
    class Meta:
        model = Listing
        exclude = ['status', 'property_type', 'contact', 'created_at', 'updated_at']
        widgets = {
            'status': Select(attrs={'class': 'form-control'}),
            'property_type': Select(attrs={'class': 'form-control'}),
            'transaction_type': Select(attrs={'class': 'form-control'}),

            'contact': Select(attrs={'class': 'form-control'}),

            'owner_name': TextInput(attrs={'class': 'form-control'}),
            'owner_phone': TextInput(attrs={'class': 'form-control'}),
            'owner_email': EmailInput(attrs={'class': 'form-control'}),

            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'county': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'zone': TextInput(attrs={'class': 'form-control'}),
            'street_address': TextInput(attrs={'class': 'form-control'}),
            'street_nr': NumberInput(attrs={'class': 'form-control'}),

            'payment_method': Select(attrs={'class': 'form-control'}),
            'other_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'created_at': DateInput(attrs={'class': 'form-control'}),
            'updated_at': DateInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        owner_name = cleaned_data.get('owner_name')
        owner_phone = cleaned_data.get('owner_phone')
        owner_email = cleaned_data.get('owner_email')
        existing_contact = cleaned_data.get('contact')

        if not existing_contact:
            if not owner_phone and not owner_email:
                raise ValidationError(
                    'Trebuie să introduci cel puțin un număr de telefon sau o adresă de e-mail pentru a crea un contact nou.'
                )
            try:
                new_contact = Contact.objects.create(
                    owner_name=owner_name,
                    owner_phone=owner_phone,
                    owner_email=owner_email,
                )
            except IntegrityError:
                raise ValidationError('Numărul de telefon sau adresa de e-mail există deja în baza de date.')
        else:
            new_contact = existing_contact

        self.cleaned_data['contact'] = new_contact

        return cleaned_data


class ApartmentCreateForm(ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'
        widgets = {
            'residential_ensemble': Select(attrs={'class': 'form-control'}),
            'block': TextInput(attrs={'class': 'form-control'}),
            'scale': TextInput(attrs={'class': 'form-control'}),
            'apartment_nr': TextInput(attrs={'class': 'form-control'}),

            'apartment_type': Select(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),
            'ap_compart': Select(attrs={'class': 'form-control'}),
            'orientation': Select(attrs={'class': 'form-control'}),
            'floor': Select(attrs={'class': 'form-control'}),
            'comfort': Select(attrs={'class': 'form-control'}),
            'interior_finishes': Select(attrs={'class': 'form-control'}),
            'useful_surface': TextInput(attrs={'class': 'form-control'}),
            'total_surface': TextInput(attrs={'class': 'form-control'}),
            'balcony_surface': TextInput(attrs={'class': 'form-control'}),
            'terrace_surface': TextInput(attrs={'class': 'form-control'}),

            'rooms_number': TextInput(attrs={'class': 'form-control'}),
            'nr_bedrooms': TextInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': TextInput(attrs={'class': 'form-control'}),
            'bathroom_window': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_balconies': TextInput(attrs={'class': 'form-control'}),
            'nr_terraces': TextInput(attrs={'class': 'form-control'}),
            'garage': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_parking_spaces': TextInput(attrs={'class': 'form-control'}),

            'building_type': Select(attrs={'class': 'form-control'}),
            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'construction_materials': SelectMultiple(attrs={'class': 'form-control'}),
            'construction_status': Select(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'attic': CheckboxInput(attrs={'class': 'form-check-input'}),

            'facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'thermal_insulation': SelectMultiple(attrs={'class': 'form-control'}),
            'building_facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'parking': SelectMultiple(attrs={'class': 'form-control'}),
            'heating_system': SelectMultiple(attrs={'class': 'form-control'}),
            'entrance_door': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_doors': SelectMultiple(attrs={'class': 'form-control'}),
            'furniture': SelectMultiple(attrs={'class': 'form-control'}),
            'kitchen': SelectMultiple(attrs={'class': 'form-control'}),
            'windows': SelectMultiple(attrs={'class': 'form-control'}),
            'other_spaces': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        useful_surface = cleaned_data.get('useful_surface')
        total_surface = cleaned_data.get('total_surface')

        if total_surface is not None and useful_surface >= total_surface:
            raise ValidationError('Suprafața utilă nu poate fi mai mare sau egală cu suprafața totală.')

        rooms_number = cleaned_data.get('rooms_number')
        bedrooms_number = cleaned_data.get('nr_bedrooms')

        if bedrooms_number is not None and bedrooms_number > rooms_number:
            raise ValidationError('Numărul de dormitoare nu poate fi mai mare decât numărul total de camere.')

        floor = cleaned_data.get('floor')
        nr_floors = cleaned_data.get('nr_floors')

        if floor > nr_floors:
            raise ValidationError('Numărul etajului apartamentului nu poate fi mai mare decât numărul total de etaje.')

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        useful_surface = cleaned_data.get('useful_surface')

        if price > 0 and useful_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(useful_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class HouseCreateForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'
        widgets = {
            'residential_ensemble': Select(attrs={'class': 'form-control'}),

            'house_type': Select(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_finishes': Select(attrs={'class': 'form-control'}),
            'useful_surface': TextInput(attrs={'class': 'form-control'}),
            'built_area': TextInput(attrs={'class': 'form-control'}),
            'terrain_surface': TextInput(attrs={'class': 'form-control'}),
            'terrain_total_surface': TextInput(attrs={'class': 'form-control'}),
            'terrace_surface': TextInput(attrs={'class': 'form-control'}),
            'balcony_surface': TextInput(attrs={'class': 'form-control'}),
            'opening': TextInput(attrs={'class': 'form-control'}),

            'roof': Select(attrs={'class': 'form-control'}),
            'construction_status': Select(attrs={'class': 'form-control'}),
            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'construction_materials': SelectMultiple(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'attic': CheckboxInput(attrs={'class': 'form-check-input'}),

            'rooms_number': TextInput(attrs={'class': 'form-control'}),
            'nr_bedrooms': TextInput(attrs={'class': 'form-control'}),
            'nr_kitchens': TextInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': TextInput(attrs={'class': 'form-control'}),
            'bathroom_window': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_terraces': TextInput(attrs={'class': 'form-control'}),
            'nr_balconies': TextInput(attrs={'class': 'form-control'}),
            'garage': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_parking_spaces': TextInput(attrs={'class': 'form-control'}),

            'facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'thermal_insulation': SelectMultiple(attrs={'class': 'form-control'}),
            'building_facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'parking': SelectMultiple(attrs={'class': 'form-control'}),
            'heating_system': SelectMultiple(attrs={'class': 'form-control'}),
            'entrance_door': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_doors': SelectMultiple(attrs={'class': 'form-control'}),
            'furniture': SelectMultiple(attrs={'class': 'form-control'}),
            'kitchen': SelectMultiple(attrs={'class': 'form-control'}),
            'windows': SelectMultiple(attrs={'class': 'form-control'}),
            'other_spaces': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        useful_surface = cleaned_data.get('useful_surface')
        built_area = cleaned_data.get('built_area')

        if built_area is not None and useful_surface >= built_area:
            raise ValidationError('Suprafața utilă nu poate fi mai mare sau egală cu suprafața construită.')

        rooms_number = cleaned_data.get('rooms_number')
        bedrooms_number = cleaned_data.get('nr_bedrooms')

        if bedrooms_number is not None and bedrooms_number > rooms_number:
            raise ValidationError('Numărul de dormitoare nu poate fi mai mare decât numărul total de camere.')

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        useful_surface = cleaned_data.get('useful_surface')

        if price > 0 and useful_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(useful_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class TerrainCreateForm(ModelForm):
    class Meta:
        model = Terrain
        fields = '__all__'
        widgets = {
            'terrain_type': Select(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),
            'classification': Select(attrs={'class': 'form-control'}),
            'terrain_surface': TextInput(attrs={'class': 'form-control'}),
            'unit': Select(attrs={'class': 'form-control'}),
            'street_front': TextInput(attrs={'class': 'form-control'}),
            'nr_street_fronts': TextInput(attrs={'class': 'form-control'}),
            'opening_to': Select(attrs={'class': 'form-control'}),
            'fusion_degree': TextInput(attrs={'class': 'form-control'}),
            'inclination': TextInput(attrs={'class': 'form-control'}),
            'incidence_value': TextInput(attrs={'class': 'form-control'}),
            'construction': CheckboxInput(attrs={'class': 'form-check-input'}),
            'construction_surface': TextInput(attrs={'class': 'form-control'}),
            'access_road_width': TextInput(attrs={'class': 'form-control'}),

            'pot': TextInput(attrs={'class': 'form-control'}),
            'cut': TextInput(attrs={'class': 'form-control'}),
            'building_permit': CheckboxInput(attrs={'class': 'form-check-input'}),
            'pug': CheckboxInput(attrs={'class': 'form-check-input'}),
            'puz': CheckboxInput(attrs={'class': 'form-check-input'}),
            'pud': CheckboxInput(attrs={'class': 'form-check-input'}),
            'urban_certificate': CheckboxInput(attrs={'class': 'form-check-input'}),
            'maximum_nr_levels': TextInput(attrs={'class': 'form-control'}),

            'land_facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'other_features': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        terrain_surface = cleaned_data.get('terrain_surface')

        if price > 0 and terrain_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(terrain_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class CommercialSpaceCreateForm(ModelForm):
    class Meta:
        model = CommercialSpace
        fields = '__all__'
        widgets = {
            'residential_ensemble': Select(attrs={'class': 'form-control'}),
            'office_building': Select(attrs={'class': 'form-control'}),
            'block': TextInput(attrs={'class': 'form-control'}),
            'space_nr': TextInput(attrs={'class': 'form-control'}),

            'space_type': Select(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),
            'pedestrian_traffic': Select(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'rooms_number': TextInput(attrs={'class': 'form-control'}),
            'nr_locker_rooms': TextInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': TextInput(attrs={'class': 'form-control'}),
            'nr_kitchens': TextInput(attrs={'class': 'form-control'}),
            'nr_terraces': TextInput(attrs={'class': 'form-control'}),
            'useful_surface': TextInput(attrs={'class': 'form-control'}),
            'total_surface': TextInput(attrs={'class': 'form-control'}),
            'street_front': TextInput(attrs={'class': 'form-control'}),
            'glass_case': TextInput(attrs={'class': 'form-control'}),
            'inside_height': TextInput(attrs={'class': 'form-control'}),
            'space_compart': Select(attrs={'class': 'form-control'}),
            'nr_parking_spaces': TextInput(attrs={'class': 'form-control'}),

            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),

            'land_facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'eco_elements': SelectMultiple(attrs={'class': 'form-control'}),
            'parking': SelectMultiple(attrs={'class': 'form-control'}),
            'other_facilities_com_sp': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        useful_surface = cleaned_data.get('useful_surface')
        total_surface = cleaned_data.get('total_surface')

        if total_surface is not None and useful_surface >= total_surface:
            raise ValidationError('Suprafața utilă nu poate fi mai mare sau egală cu suprafața totală.')

        floor = cleaned_data.get('floor')
        nr_floors = cleaned_data.get('nr_floors')

        if floor > nr_floors:
            raise ValidationError('Numărul etajului spațiului comercial nu poate fi mai mare decât numărul total de etaje.')

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        useful_surface = cleaned_data.get('useful_surface')

        if price > 0 and useful_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(useful_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class OfficeSpaceCreateForm(ModelForm):
    class Meta:
        model = OfficeSpace
        fields = '__all__'
        widgets = {
            'office_building': Select(attrs={'class': 'form-control'}),
            'space_nr': TextInput(attrs={'class': 'form-control'}),

            'space_type': Select(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'space_class': Select(attrs={'class': 'form-control'}),
            'rooms_number': TextInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': TextInput(attrs={'class': 'form-control'}),
            'useful_surface': TextInput(attrs={'class': 'form-control'}),
            'total_surface': TextInput(attrs={'class': 'form-control'}),
            'nr_terraces': TextInput(attrs={'class': 'form-control'}),

            'minimum_area': TextInput(attrs={'class': 'form-control'}),
            'maximum_area': TextInput(attrs={'class': 'form-control'}),
            'total_surface_offices': TextInput(attrs={'class': 'form-control'}),
            'common_area_factor': TextInput(attrs={'class': 'form-control'}),
            'occupancy_rate': TextInput(attrs={'class': 'form-control'}),
            'space_compart': Select(attrs={'class': 'form-control'}),

            'underground_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'underground_parking_available': TextInput(attrs={'class': 'form-control'}),
            'underground_parking_cost': TextInput(attrs={'class': 'form-control'}),
            'surface_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'surface_parking_available': TextInput(attrs={'class': 'form-control'}),
            'surface_parking_cost': TextInput(attrs={'class': 'form-control'}),

            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'nr_elevators': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),

            'services_provided': SelectMultiple(attrs={'class': 'form-control'}),
            'safety_security': SelectMultiple(attrs={'class': 'form-control'}),
            'it_c': SelectMultiple(attrs={'class': 'form-control'}),
            'electrical_system': SelectMultiple(attrs={'class': 'form-control'}),
            'eco_elements': SelectMultiple(attrs={'class': 'form-control'}),
            'architecture': SelectMultiple(attrs={'class': 'form-control'}),
            'air_conditioning': SelectMultiple(attrs={'class': 'form-control'}),
            'building_facilities_proximity': SelectMultiple(attrs={'class': 'form-control'}),
            'parking': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        useful_surface = cleaned_data.get('useful_surface')
        total_surface = cleaned_data.get('total_surface')

        if total_surface is not None and useful_surface >= total_surface:
            raise ValidationError('Suprafața utilă nu poate fi mai mare sau egală cu suprafața totală.')

        minimum_area = cleaned_data.get('minimum_area')
        maximum_area = cleaned_data.get('maximum_area')

        if minimum_area is not None and maximum_area is not None and minimum_area >= maximum_area:
            raise ValidationError('Suprafața minimă nu poate fi mai mare sau egală cu suprafața maximă.')

        floor = cleaned_data.get('floor')
        nr_floors = cleaned_data.get('nr_floors')

        if floor > nr_floors:
            raise ValidationError('Numărul etajului spațiului de birou nu poate fi mai mare decât numărul total de etaje.')

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        useful_surface = cleaned_data.get('useful_surface')

        if price > 0 and useful_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(useful_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class IndustrialSpaceCreateForm(ModelForm):
    class Meta:
        model = IndustrialSpace
        fields = '__all__'
        widgets = {
            'space_type': Select(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'space_class': Select(attrs={'class': 'form-control'}),
            'rooms_number': TextInput(attrs={'class': 'form-control'}),
            'nr_locker_rooms': TextInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': TextInput(attrs={'class': 'form-control'}),
            'nr_kitchens': TextInput(attrs={'class': 'form-control'}),
            'nr_terraces': TextInput(attrs={'class': 'form-control'}),

            'useful_surface': TextInput(attrs={'class': 'form-control'}),
            'built_area': TextInput(attrs={'class': 'form-control'}),
            'total_surface_offices': TextInput(attrs={'class': 'form-control'}),
            'space_compart': Select(attrs={'class': 'form-control'}),
            'glass_case': TextInput(attrs={'class': 'form-control'}),
            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'terrain_surface': TextInput(attrs={'class': 'form-control'}),
            'production_area': TextInput(attrs={'class': 'form-control'}),
            'storage_area': TextInput(attrs={'class': 'form-control'}),
            'entrance_door_dimensions': TextInput(attrs={'class': 'form-control'}),
            'inside_height': TextInput(attrs={'class': 'form-control'}),
            'nr_parking_spaces': TextInput(attrs={'class': 'form-control'}),

            'land_facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'parking': SelectMultiple(attrs={'class': 'form-control'}),
            'other_facilities_ind_sp': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        useful_surface = cleaned_data.get('useful_surface')
        built_area = cleaned_data.get('built_area')

        if built_area is not None and useful_surface >= built_area:
            raise ValidationError('Suprafața utilă nu poate fi mai mare sau egală cu suprafața construită.')

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        useful_surface = cleaned_data.get('useful_surface')

        if price > 0 and useful_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(useful_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class ResidentialEnsembleCreateForm(ModelForm):
    contact = ModelChoiceField(queryset=Contact.objects.all(), required=False, label='Contact asociat',
                               widget=Select(attrs={'class': 'form-control'}))
    images = MultiImageField(required=False)
    class Meta:
        model = ResidentialEnsemble
        exclude = ['created_at', 'updated_at']
        widgets = {
            'status': Select(attrs={'class': 'form-control'}),

            'developer_name': TextInput(attrs={'class': 'form-control'}),
            'developer_phone': TextInput(attrs={'class': 'form-control'}),
            'developer_email': EmailInput(attrs={'class': 'form-control'}),

            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'county': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'zone': TextInput(attrs={'class': 'form-control'}),
            'street_address': TextInput(attrs={'class': 'form-control'}),
            'street_nr': NumberInput(attrs={'class': 'form-control'}),

            'building_type': Select(attrs={'class': 'form-control'}),
            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'construction_status': Select(attrs={'class': 'form-control'}),
            'construction_materials': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_finishes': Select(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'attic': CheckboxInput(attrs={'class': 'form-check-input'}),

            'underground_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_underground_parking': TextInput(attrs={'class': 'form-control'}),
            'underground_parking_cost': TextInput(attrs={'class': 'form-control'}),
            'surface_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_surface_parking': TextInput(attrs={'class': 'form-control'}),
            'surface_parking_cost': TextInput(attrs={'class': 'form-control'}),

            'finishes': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'technical_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'thermal_insulation': SelectMultiple(attrs={'class': 'form-control'}),
            'other_spaces': SelectMultiple(attrs={'class': 'form-control'}),

            'other_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'created_at': DateInput(attrs={'class': 'form-control'}),
            'updated_at': DateInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        developer_name = cleaned_data.get('developer_name')
        developer_phone = cleaned_data.get('developer_phone')
        developer_email = cleaned_data.get('developer_email')
        existing_contact = cleaned_data.get('contact')

        if not existing_contact:
            if not developer_phone and not developer_email:
                raise ValidationError(
                    'Trebuie să introduci cel puțin un număr de telefon sau o adresă de e-mail pentru a crea un contact nou.'
                )
            try:
                new_contact = Contact.objects.create(
                    developer_name=developer_name,
                    developer_phone=developer_phone,
                    developer_email=developer_email,
                )
            except IntegrityError:
                raise ValidationError('Numărul de telefon sau adresa de e-mail există deja în baza de date.')
        else:
            new_contact = existing_contact

        self.cleaned_data['contact'] = new_contact

        return cleaned_data


class OfficeBuildingCreateForm(ModelForm):
    contact = ModelChoiceField(queryset=Contact.objects.all(), required=False, label='Contact asociat',
                               widget=Select(attrs={'class': 'form-control'}))
    images = MultiImageField(required=False)
    class Meta:
        model = OfficeBuilding
        exclude = ['created_at', 'updated_at']
        widgets = {
            'status': Select(attrs={'class': 'form-control'}),

            'developer_name': TextInput(attrs={'class': 'form-control'}),
            'developer_phone': TextInput(attrs={'class': 'form-control'}),
            'developer_email': EmailInput(attrs={'class': 'form-control'}),

            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'county': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'zone': TextInput(attrs={'class': 'form-control'}),
            'street_address': TextInput(attrs={'class': 'form-control'}),
            'street_nr': NumberInput(attrs={'class': 'form-control'}),

            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'construction_status': Select(attrs={'class': 'form-control'}),
            'construction_materials': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_finishes': Select(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'space_class': Select(attrs={'class': 'form-control'}),
            'minimum_area': TextInput(attrs={'class': 'form-control'}),
            'maximum_area': TextInput(attrs={'class': 'form-control'}),
            'total_surface_offices': TextInput(attrs={'class': 'form-control'}),
            'common_area_factor': TextInput(attrs={'class': 'form-control'}),
            'occupancy_rate': TextInput(attrs={'class': 'form-control'}),

            'underground_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_underground_parking': TextInput(attrs={'class': 'form-control'}),
            'underground_parking_cost': TextInput(attrs={'class': 'form-control'}),
            'surface_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_surface_parking': TextInput(attrs={'class': 'form-control'}),
            'surface_parking_cost': TextInput(attrs={'class': 'form-control'}),

            'nr_elevators': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'mezzanine': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),

            'finishes': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'technical_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'services_provided': SelectMultiple(attrs={'class': 'form-control'}),
            'safety_security': SelectMultiple(attrs={'class': 'form-control'}),
            'it_c': SelectMultiple(attrs={'class': 'form-control'}),
            'electrical_system': SelectMultiple(attrs={'class': 'form-control'}),
            'eco_elements': SelectMultiple(attrs={'class': 'form-control'}),
            'architecture': SelectMultiple(attrs={'class': 'form-control'}),
            'air_conditioning': SelectMultiple(attrs={'class': 'form-control'}),
            'building_facilities_proximity': SelectMultiple(attrs={'class': 'form-control'}),

            'other_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'created_at': DateInput(attrs={'class': 'form-control'}),
            'updated_at': DateInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        minimum_area = cleaned_data.get('minimum_area')
        maximum_area = cleaned_data.get('maximum_area')

        if minimum_area is not None and maximum_area is not None and minimum_area >= maximum_area:
            raise ValidationError('Suprafața minimă nu poate fi mai mare sau egală cu suprafața maximă.')

        developer_name = cleaned_data.get('developer_name')
        developer_phone = cleaned_data.get('developer_phone')
        developer_email = cleaned_data.get('developer_email')
        existing_contact = cleaned_data.get('contact')

        if not existing_contact:
            if not developer_phone and not developer_email:
                raise ValidationError(
                    'Trebuie să introduci cel puțin un număr de telefon sau o adresă de e-mail pentru a crea un contact nou.'
                )
            try:
                new_contact = Contact.objects.create(
                    developer_name=developer_name,
                    developer_phone=developer_phone,
                    developer_email=developer_email,
                )
            except IntegrityError:
                raise ValidationError('Numărul de telefon sau adresa de e-mail există deja în baza de date.')
        else:
            new_contact = existing_contact

        self.cleaned_data['contact'] = new_contact

        return cleaned_data


########################################################################################################################
#                               ---   FORMULARE ACTUALIZARE   ---

class ListingUpdateForm(ModelForm):
    images = MultiImageField(required=False)
    class Meta:
        model = Listing
        fields = '__all__'
        widgets = {
            'status': Select(attrs={'class': 'form-control'}),
            'property_type': TextInput(attrs={'readonly': 'readonly'}),
            'transaction_type': TextInput(attrs={'readonly': 'readonly'}),

            'contact': TextInput(attrs={'readonly': 'readonly'}),

            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'county': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'zone': TextInput(attrs={'class': 'form-control'}),
            'street_address': TextInput(attrs={'class': 'form-control'}),
            'street_nr': NumberInput(attrs={'class': 'form-control'}),

            'payment_method': Select(attrs={'class': 'form-control'}),
            'other_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'created_at': DateInput(attrs={'readonly': 'readonly'}),
            'updated_at': DateInput(attrs={'readonly': 'readonly'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        owner_name = cleaned_data.get('owner_name')
        owner_phone = cleaned_data.get('owner_phone')
        owner_email = cleaned_data.get('owner_email')
        existing_contact = cleaned_data.get('contact')

        if not existing_contact:
            if not owner_phone and not owner_email:
                raise ValidationError(
                    'Trebuie să introduci cel puțin un număr de telefon sau o adresă de e-mail pentru a crea un contact nou.'
                )
            try:
                new_contact = Contact.objects.create(
                    owner_name=owner_name,
                    owner_phone=owner_phone,
                    owner_email=owner_email,
                )
            except IntegrityError:
                raise ValidationError('Numărul de telefon sau adresa de e-mail există deja în baza de date.')
        else:
            new_contact = existing_contact

        self.cleaned_data['contact'] = new_contact

        return cleaned_data


class ApartmentUpdateForm(ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'
        widgets = {
            'residential_ensemble': Select(attrs={'class': 'form-control'}),
            'block': TextInput(attrs={'class': 'form-control'}),
            'scale': TextInput(attrs={'class': 'form-control'}),
            'apartment_nr': TextInput(attrs={'class': 'form-control'}),

            'apartment_type': Select(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),
            'ap_compart': Select(attrs={'class': 'form-control'}),
            'orientation': Select(attrs={'class': 'form-control'}),
            'floor': Select(attrs={'class': 'form-control'}),
            'comfort': Select(attrs={'class': 'form-control'}),
            'interior_finishes': Select(attrs={'class': 'form-control'}),
            'useful_surface': TextInput(attrs={'class': 'form-control'}),
            'total_surface': TextInput(attrs={'class': 'form-control'}),
            'balcony_surface': TextInput(attrs={'class': 'form-control'}),
            'terrace_surface': TextInput(attrs={'class': 'form-control'}),

            'rooms_number': TextInput(attrs={'class': 'form-control'}),
            'nr_bedrooms': TextInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': TextInput(attrs={'class': 'form-control'}),
            'bathroom_window': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_balconies': TextInput(attrs={'class': 'form-control'}),
            'nr_terraces': TextInput(attrs={'class': 'form-control'}),
            'garage': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_parking_spaces': TextInput(attrs={'class': 'form-control'}),

            'building_type': Select(attrs={'class': 'form-control'}),
            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'construction_materials': SelectMultiple(attrs={'class': 'form-control'}),
            'construction_status': Select(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'attic': CheckboxInput(attrs={'class': 'form-check-input'}),

            'facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'thermal_insulation': SelectMultiple(attrs={'class': 'form-control'}),
            'building_facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'parking': SelectMultiple(attrs={'class': 'form-control'}),
            'heating_system': SelectMultiple(attrs={'class': 'form-control'}),
            'entrance_door': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_doors': SelectMultiple(attrs={'class': 'form-control'}),
            'furniture': SelectMultiple(attrs={'class': 'form-control'}),
            'kitchen': SelectMultiple(attrs={'class': 'form-control'}),
            'windows': SelectMultiple(attrs={'class': 'form-control'}),
            'other_spaces': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        useful_surface = cleaned_data.get('useful_surface')
        total_surface = cleaned_data.get('total_surface')

        if total_surface is not None and useful_surface >= total_surface:
            raise ValidationError('Suprafața utilă nu poate fi mai mare sau egală cu suprafața totală.')

        rooms_number = cleaned_data.get('rooms_number')
        bedrooms_number = cleaned_data.get('nr_bedrooms')

        if bedrooms_number is not None and bedrooms_number > rooms_number:
            raise ValidationError('Numărul de dormitoare nu poate fi mai mare decât numărul total de camere.')

        floor = cleaned_data.get('floor')
        nr_floors = cleaned_data.get('nr_floors')

        if floor > nr_floors:
            raise ValidationError('Numărul etajului apartamentului nu poate fi mai mare decât numărul total de etaje.')

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        useful_surface = cleaned_data.get('useful_surface')

        if price > 0 and useful_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(useful_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class HouseUpdateForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'
        widgets = {
            'residential_ensemble': Select(attrs={'class': 'form-control'}),

            'house_type': Select(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_finishes': Select(attrs={'class': 'form-control'}),
            'useful_surface': TextInput(attrs={'class': 'form-control'}),
            'built_area': TextInput(attrs={'class': 'form-control'}),
            'terrain_surface': TextInput(attrs={'class': 'form-control'}),
            'terrain_total_surface': TextInput(attrs={'class': 'form-control'}),
            'terrace_surface': TextInput(attrs={'class': 'form-control'}),
            'balcony_surface': TextInput(attrs={'class': 'form-control'}),
            'opening': TextInput(attrs={'class': 'form-control'}),

            'roof': Select(attrs={'class': 'form-control'}),
            'construction_status': Select(attrs={'class': 'form-control'}),
            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'construction_materials': SelectMultiple(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'attic': CheckboxInput(attrs={'class': 'form-check-input'}),

            'rooms_number': TextInput(attrs={'class': 'form-control'}),
            'nr_bedrooms': TextInput(attrs={'class': 'form-control'}),
            'nr_kitchens': TextInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': TextInput(attrs={'class': 'form-control'}),
            'bathroom_window': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_terraces': TextInput(attrs={'class': 'form-control'}),
            'nr_balconies': TextInput(attrs={'class': 'form-control'}),
            'garage': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_parking_spaces': TextInput(attrs={'class': 'form-control'}),

            'facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'thermal_insulation': SelectMultiple(attrs={'class': 'form-control'}),
            'building_facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'parking': SelectMultiple(attrs={'class': 'form-control'}),
            'heating_system': SelectMultiple(attrs={'class': 'form-control'}),
            'entrance_door': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_doors': SelectMultiple(attrs={'class': 'form-control'}),
            'furniture': SelectMultiple(attrs={'class': 'form-control'}),
            'kitchen': SelectMultiple(attrs={'class': 'form-control'}),
            'windows': SelectMultiple(attrs={'class': 'form-control'}),
            'other_spaces': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        useful_surface = cleaned_data.get('useful_surface')
        built_area = cleaned_data.get('built_area')

        if built_area is not None and useful_surface >= built_area:
            raise ValidationError('Suprafața utilă nu poate fi mai mare sau egală cu suprafața construită.')

        rooms_number = cleaned_data.get('rooms_number')
        bedrooms_number = cleaned_data.get('nr_bedrooms')

        if bedrooms_number is not None and bedrooms_number > rooms_number:
            raise ValidationError('Numărul de dormitoare nu poate fi mai mare decât numărul total de camere.')

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        useful_surface = cleaned_data.get('useful_surface')

        if price > 0 and useful_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(useful_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class TerrainUpdateForm(ModelForm):
    class Meta:
        model = Terrain
        fields = '__all__'
        widgets = {
            'terrain_type': Select(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),
            'classification': Select(attrs={'class': 'form-control'}),
            'terrain_surface': TextInput(attrs={'class': 'form-control'}),
            'unit': Select(attrs={'class': 'form-control'}),
            'street_front': TextInput(attrs={'class': 'form-control'}),
            'nr_street_fronts': TextInput(attrs={'class': 'form-control'}),
            'opening_to': Select(attrs={'class': 'form-control'}),
            'fusion_degree': TextInput(attrs={'class': 'form-control'}),
            'inclination': TextInput(attrs={'class': 'form-control'}),
            'incidence_value': TextInput(attrs={'class': 'form-control'}),
            'construction': CheckboxInput(attrs={'class': 'form-check-input'}),
            'construction_surface': TextInput(attrs={'class': 'form-control'}),
            'access_road_width': TextInput(attrs={'class': 'form-control'}),

            'pot': TextInput(attrs={'class': 'form-control'}),
            'cut': TextInput(attrs={'class': 'form-control'}),
            'building_permit': CheckboxInput(attrs={'class': 'form-check-input'}),
            'pug': CheckboxInput(attrs={'class': 'form-check-input'}),
            'puz': CheckboxInput(attrs={'class': 'form-check-input'}),
            'pud': CheckboxInput(attrs={'class': 'form-check-input'}),
            'urban_certificate': CheckboxInput(attrs={'class': 'form-check-input'}),
            'maximum_nr_levels': TextInput(attrs={'class': 'form-control'}),

            'land_facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'other_features': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        terrain_surface = cleaned_data.get('terrain_surface')

        if price > 0 and terrain_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(terrain_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class CommercialSpaceUpdateForm(ModelForm):
    class Meta:
        model = CommercialSpace
        fields = '__all__'
        widgets = {
            'residential_ensemble': Select(attrs={'class': 'form-control'}),
            'office_building': Select(attrs={'class': 'form-control'}),
            'block': TextInput(attrs={'class': 'form-control'}),
            'space_nr': TextInput(attrs={'class': 'form-control'}),

            'space_type': Select(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),
            'pedestrian_traffic': Select(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'rooms_number': TextInput(attrs={'class': 'form-control'}),
            'nr_locker_rooms': TextInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': TextInput(attrs={'class': 'form-control'}),
            'nr_kitchens': TextInput(attrs={'class': 'form-control'}),
            'nr_terraces': TextInput(attrs={'class': 'form-control'}),
            'useful_surface': TextInput(attrs={'class': 'form-control'}),
            'total_surface': TextInput(attrs={'class': 'form-control'}),
            'street_front': TextInput(attrs={'class': 'form-control'}),
            'glass_case': TextInput(attrs={'class': 'form-control'}),
            'inside_height': TextInput(attrs={'class': 'form-control'}),
            'space_compart': Select(attrs={'class': 'form-control'}),
            'nr_parking_spaces': TextInput(attrs={'class': 'form-control'}),

            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),

            'land_facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'eco_elements': SelectMultiple(attrs={'class': 'form-control'}),
            'parking': SelectMultiple(attrs={'class': 'form-control'}),
            'other_facilities_com_sp': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        useful_surface = cleaned_data.get('useful_surface')
        total_surface = cleaned_data.get('total_surface')

        if total_surface is not None and useful_surface >= total_surface:
            raise ValidationError('Suprafața utilă nu poate fi mai mare sau egală cu suprafața totală.')

        floor = cleaned_data.get('floor')
        nr_floors = cleaned_data.get('nr_floors')

        if floor > nr_floors:
            raise ValidationError('Numărul etajului spațiului comercial nu poate fi mai mare decât numărul total de etaje.')

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        useful_surface = cleaned_data.get('useful_surface')

        if price > 0 and useful_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(useful_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class OfficeSpaceUpdateForm(ModelForm):
    class Meta:
        model = OfficeSpace
        fields = '__all__'
        widgets = {
            'office_building': Select(attrs={'class': 'form-control'}),
            'space_nr': TextInput(attrs={'class': 'form-control'}),

            'space_type': Select(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'space_class': Select(attrs={'class': 'form-control'}),
            'rooms_number': TextInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': TextInput(attrs={'class': 'form-control'}),
            'useful_surface': TextInput(attrs={'class': 'form-control'}),
            'total_surface': TextInput(attrs={'class': 'form-control'}),
            'nr_terraces': TextInput(attrs={'class': 'form-control'}),

            'minimum_area': TextInput(attrs={'class': 'form-control'}),
            'maximum_area': TextInput(attrs={'class': 'form-control'}),
            'total_surface_offices': TextInput(attrs={'class': 'form-control'}),
            'common_area_factor': TextInput(attrs={'class': 'form-control'}),
            'occupancy_rate': TextInput(attrs={'class': 'form-control'}),
            'space_compart': Select(attrs={'class': 'form-control'}),

            'underground_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'underground_parking_available': TextInput(attrs={'class': 'form-control'}),
            'underground_parking_cost': TextInput(attrs={'class': 'form-control'}),
            'surface_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'surface_parking_available': TextInput(attrs={'class': 'form-control'}),
            'surface_parking_cost': TextInput(attrs={'class': 'form-control'}),

            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'nr_elevators': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),

            'services_provided': SelectMultiple(attrs={'class': 'form-control'}),
            'safety_security': SelectMultiple(attrs={'class': 'form-control'}),
            'it_c': SelectMultiple(attrs={'class': 'form-control'}),
            'electrical_system': SelectMultiple(attrs={'class': 'form-control'}),
            'eco_elements': SelectMultiple(attrs={'class': 'form-control'}),
            'architecture': SelectMultiple(attrs={'class': 'form-control'}),
            'air_conditioning': SelectMultiple(attrs={'class': 'form-control'}),
            'building_facilities_proximity': SelectMultiple(attrs={'class': 'form-control'}),
            'parking': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        useful_surface = cleaned_data.get('useful_surface')
        total_surface = cleaned_data.get('total_surface')

        if total_surface is not None and useful_surface >= total_surface:
            raise ValidationError('Suprafața utilă nu poate fi mai mare sau egală cu suprafața totală.')

        minimum_area = cleaned_data.get('minimum_area')
        maximum_area = cleaned_data.get('maximum_area')

        if minimum_area is not None and maximum_area is not None and minimum_area >= maximum_area:
            raise ValidationError('Suprafața minimă nu poate fi mai mare sau egală cu suprafața maximă.')

        floor = cleaned_data.get('floor')
        nr_floors = cleaned_data.get('nr_floors')

        if floor > nr_floors:
            raise ValidationError('Numărul etajului spațiului de birou nu poate fi mai mare decât numărul total de etaje.')

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        useful_surface = cleaned_data.get('useful_surface')

        if price > 0 and useful_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(useful_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class IndustrialSpaceUpdateForm(ModelForm):
    class Meta:
        model = IndustrialSpace
        fields = '__all__'
        widgets = {
            'space_type': Select(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'space_class': Select(attrs={'class': 'form-control'}),
            'rooms_number': TextInput(attrs={'class': 'form-control'}),
            'nr_locker_rooms': TextInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': TextInput(attrs={'class': 'form-control'}),
            'nr_kitchens': TextInput(attrs={'class': 'form-control'}),
            'nr_terraces': TextInput(attrs={'class': 'form-control'}),

            'useful_surface': TextInput(attrs={'class': 'form-control'}),
            'built_area': TextInput(attrs={'class': 'form-control'}),
            'total_surface_offices': TextInput(attrs={'class': 'form-control'}),
            'space_compart': Select(attrs={'class': 'form-control'}),
            'glass_case': TextInput(attrs={'class': 'form-control'}),
            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'terrain_surface': TextInput(attrs={'class': 'form-control'}),
            'production_area': TextInput(attrs={'class': 'form-control'}),
            'storage_area': TextInput(attrs={'class': 'form-control'}),
            'entrance_door_dimensions': TextInput(attrs={'class': 'form-control'}),
            'inside_height': TextInput(attrs={'class': 'form-control'}),
            'nr_parking_spaces': TextInput(attrs={'class': 'form-control'}),

            'land_facilities': SelectMultiple(attrs={'class': 'form-control'}),
            'parking': SelectMultiple(attrs={'class': 'form-control'}),
            'other_facilities_ind_sp': SelectMultiple(attrs={'class': 'form-control'}),

            'price': TextInput(attrs={'class': 'form-control'}),
            'last_price': TextInput(attrs={'class': 'form-control'}),
            'negotiable': CheckboxInput(attrs={'class': 'form-control'}),
            'price_per_sqm': TextInput(attrs={'readonly': 'readonly'}),
            'owner_type': Select(attrs={'class': 'form-control'}),
            'VAT_rate': Select(attrs={'class': 'form-control'}),
            'currency': Select(attrs={'class': 'form-control'}),
            'percentage_commission': TextInput(attrs={'class': 'form-control'}),
            'fixed_commission': TextInput(attrs={'class': 'form-control'}),
            'exclusive_representation': CheckboxInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        useful_surface = cleaned_data.get('useful_surface')
        built_area = cleaned_data.get('built_area')

        if built_area is not None and useful_surface >= built_area:
            raise ValidationError('Suprafața utilă nu poate fi mai mare sau egală cu suprafața construită.')

        price = cleaned_data.get('price')
        last_price = cleaned_data.get('last_price')

        if last_price is not None and price <= last_price:
            raise ValidationError('Prețul de tranzacționare nu poate fi mai mic sau egal cu prețul cerut în mână.')

        price = cleaned_data.get('price')
        useful_surface = cleaned_data.get('useful_surface')

        if price > 0 and useful_surface > 0:
            price_per_sqm = Decimal(price) / Decimal(useful_surface)
            self.cleaned_data['price_per_sqm'] = price_per_sqm
        else:
            self.fields['price_per_sqm'].widget = HiddenInput()

        return cleaned_data


class ResidentialEnsembleUpdateForm(ModelForm):
    contact = ModelChoiceField(queryset=Contact.objects.all(), required=False, label='Contact asociat',
                               widget=Select(attrs={'class': 'form-control'}))
    images = MultiImageField(required=False)
    class Meta:
        model = ResidentialEnsemble
        fields = '__all__'
        widgets = {
            'status': Select(attrs={'class': 'form-control'}),

            'developer_name': TextInput(attrs={'class': 'form-control'}),
            'developer_phone': TextInput(attrs={'class': 'form-control'}),
            'developer_email': EmailInput(attrs={'class': 'form-control'}),

            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'county': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'zone': TextInput(attrs={'class': 'form-control'}),
            'street_address': TextInput(attrs={'class': 'form-control'}),
            'street_nr': NumberInput(attrs={'class': 'form-control'}),

            'building_type': Select(attrs={'class': 'form-control'}),
            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'construction_status': Select(attrs={'class': 'form-control'}),
            'construction_materials': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_finishes': Select(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'attic': CheckboxInput(attrs={'class': 'form-check-input'}),

            'underground_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_underground_parking': TextInput(attrs={'class': 'form-control'}),
            'underground_parking_cost': TextInput(attrs={'class': 'form-control'}),
            'surface_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_surface_parking': TextInput(attrs={'class': 'form-control'}),
            'surface_parking_cost': TextInput(attrs={'class': 'form-control'}),

            'finishes': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'technical_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'thermal_insulation': SelectMultiple(attrs={'class': 'form-control'}),
            'other_spaces': SelectMultiple(attrs={'class': 'form-control'}),

            'other_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'created_at': DateInput(attrs={'readonly': 'readonly'}),
            'updated_at': DateInput(attrs={'readonly': 'readonly'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        developer_name = cleaned_data.get('developer_name')
        developer_phone = cleaned_data.get('developer_phone')
        developer_email = cleaned_data.get('developer_email')
        existing_contact = cleaned_data.get('contact')

        if not existing_contact:
            if not developer_phone and not developer_email:
                raise ValidationError(
                    'Trebuie să introduci cel puțin un număr de telefon sau o adresă de e-mail pentru a crea un contact nou.'
                )
            try:
                new_contact = Contact.objects.create(
                    developer_name=developer_name,
                    developer_phone=developer_phone,
                    developer_email=developer_email,
                )
            except IntegrityError:
                raise ValidationError('Numărul de telefon sau adresa de e-mail există deja în baza de date.')
        else:
            new_contact = existing_contact

        self.cleaned_data['contact'] = new_contact

        return cleaned_data


class OfficeBuildingUpdateForm(ModelForm):
    contact = ModelChoiceField(queryset=Contact.objects.all(), required=False, label='Contact asociat',
                               widget=Select(attrs={'class': 'form-control'}))
    images = MultiImageField(required=False)
    class Meta:
        model = OfficeBuilding
        fields = '__all__'
        widgets = {
            'status': Select(attrs={'class': 'form-control'}),

            'developer_name': TextInput(attrs={'class': 'form-control'}),
            'developer_phone': TextInput(attrs={'class': 'form-control'}),
            'developer_email': EmailInput(attrs={'class': 'form-control'}),

            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'county': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'zone': TextInput(attrs={'class': 'form-control'}),
            'street_address': TextInput(attrs={'class': 'form-control'}),
            'street_nr': NumberInput(attrs={'class': 'form-control'}),

            'construction_year': TextInput(attrs={'class': 'form-control'}),
            'construction_status': Select(attrs={'class': 'form-control'}),
            'construction_materials': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_finishes': Select(attrs={'class': 'form-control'}),
            'nr_floors': TextInput(attrs={'class': 'form-control'}),
            'space_class': Select(attrs={'class': 'form-control'}),
            'minimum_area': TextInput(attrs={'class': 'form-control'}),
            'maximum_area': TextInput(attrs={'class': 'form-control'}),
            'total_surface_offices': TextInput(attrs={'class': 'form-control'}),
            'common_area_factor': TextInput(attrs={'class': 'form-control'}),
            'occupancy_rate': TextInput(attrs={'class': 'form-control'}),

            'underground_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_underground_parking': TextInput(attrs={'class': 'form-control'}),
            'underground_parking_cost': TextInput(attrs={'class': 'form-control'}),
            'surface_parking': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_surface_parking': TextInput(attrs={'class': 'form-control'}),
            'surface_parking_cost': TextInput(attrs={'class': 'form-control'}),

            'nr_elevators': TextInput(attrs={'class': 'form-control'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'mezzanine': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),

            'finishes': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'technical_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'services_provided': SelectMultiple(attrs={'class': 'form-control'}),
            'safety_security': SelectMultiple(attrs={'class': 'form-control'}),
            'it_c': SelectMultiple(attrs={'class': 'form-control'}),
            'electrical_system': SelectMultiple(attrs={'class': 'form-control'}),
            'eco_elements': SelectMultiple(attrs={'class': 'form-control'}),
            'architecture': SelectMultiple(attrs={'class': 'form-control'}),
            'air_conditioning': SelectMultiple(attrs={'class': 'form-control'}),
            'building_facilities_proximity': SelectMultiple(attrs={'class': 'form-control'}),

            'other_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'created_at': DateInput(attrs={'readonly': 'readonly'}),
            'updated_at': DateInput(attrs={'readonly': 'readonly'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        minimum_area = cleaned_data.get('minimum_area')
        maximum_area = cleaned_data.get('maximum_area')

        if minimum_area is not None and maximum_area is not None and minimum_area >= maximum_area:
            raise ValidationError('Suprafața minimă nu poate fi mai mare sau egală cu suprafața maximă.')

        developer_name = cleaned_data.get('developer_name')
        developer_phone = cleaned_data.get('developer_phone')
        developer_email = cleaned_data.get('developer_email')
        existing_contact = cleaned_data.get('contact')

        if not existing_contact:
            if not developer_phone and not developer_email:
                raise ValidationError(
                    'Trebuie să introduci cel puțin un număr de telefon sau o adresă de e-mail pentru a crea un contact nou.'
                )
            try:
                new_contact = Contact.objects.create(
                    developer_name=developer_name,
                    developer_phone=developer_phone,
                    developer_email=developer_email,
                )
            except IntegrityError:
                raise ValidationError('Numărul de telefon sau adresa de e-mail există deja în baza de date.')
        else:
            new_contact = existing_contact

        self.cleaned_data['contact'] = new_contact

        return cleaned_data
