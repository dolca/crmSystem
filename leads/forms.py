from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select, TextInput, Textarea, DateInput, SelectMultiple, NumberInput, CheckboxInput
from leads.models import Lead, ApartmentLead, HouseLead, TerrainLead, CommercialSpaceLead, OfficeSpaceLead, \
    IndustrialSpaceLead


########################################################################################################################
#                               ---   FORMULARE CREARE   ---

class LeadCreateForm(ModelForm):
    class Meta:
        model = Lead
        exclude = ['status', 'labels', 'notes', 'created_at', 'updated_at']
        widgets = {
            'status': Select(attrs={'class': 'form-control'}),
            'property_type': Select(attrs={'readonly': 'readonly'}),
            'transaction_type': Select(attrs={'class': 'form-control'}),

            'contact': Select(attrs={'readonly': 'readonly'}),

            'county': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'zone': TextInput(attrs={'class': 'form-control'}),
            'street': TextInput(attrs={'class': 'form-control'}),

            'budget': TextInput(attrs={'class': 'form-control'}),
            'payment_method': Select(attrs={'class': 'form-control'}),

            'urgency': Select(attrs={'class': 'form-control'}),
            'other_details': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'labels': Select(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'created_at': DateInput(attrs={'class': 'form-control'}),
            'updated_at': DateInput(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()

        phone_number = cleaned_data.get('phone_number')
        email = cleaned_data.get('email')
        errors = {}

        if not phone_number and not email:
            errors[
                'phone_number'] = 'Trebuie să introduci obligatoriu un număr de telefon sau o adresă de e-mail pentru contact.'

        if phone_number:
            check_phone_number = Lead.objects.filter(phone_number=phone_number)
            if check_phone_number.exists():
                msg = f'''Există deja un contact cu acest număr de telefon. 
                Introdu alt număr de telefon sau actualizează contactul deja existent.'''
                errors['phone_number'] = msg

        if email:
            check_email = Lead.objects.filter(email=email)
            if check_email.exists():
                msg = f'''Există deja un contact cu această adresă de e-mail. 
                Introdu altă adresă de e-mail sau actualizează contactul deja existent.'''
                errors['email'] = msg

        if errors:
            raise ValidationError(errors)

        return cleaned_data


class ApartmentLeadCreateForm(ModelForm):
    class Meta:
        model = ApartmentLead
        fields = '__all__'
        widgets = {
            'apartment_type': SelectMultiple(attrs={'class': 'form-control'}),
            'destination': Select(attrs={'class': 'form-control'}),

            'rooms_number': NumberInput(attrs={'class': 'form-control'}),
            'nr_bedrooms': NumberInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': NumberInput(attrs={'class': 'form-control'}),
            'bathroom_window': CheckboxInput(attrs={'class': 'form-check-input'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'excluded_ground_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'excluding_top_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_floors': NumberInput(attrs={'class': 'form-control'}),

            'minimal_surface': NumberInput(attrs={'class': 'form-control'}),
            'construction_status': SelectMultiple(attrs={'class': 'form-control'}),
            'furniture': SelectMultiple(attrs={'class': 'form-control'}),
            'comfort': SelectMultiple(attrs={'class': 'form-control'}),
            'ap_compart': SelectMultiple(attrs={'class': 'form-control'}),
            'orientation': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_finishes': SelectMultiple(attrs={'class': 'form-control'}),
            'construction_year': NumberInput(attrs={'class': 'form-control'}),

            'basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'attic': CheckboxInput(attrs={'class': 'form-check-input'}),
            'elevator': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        rooms_number = cleaned_data.get('rooms_number')
        bedrooms_number = cleaned_data.get('nr_bedrooms')

        if bedrooms_number is not None and rooms_number is not None and bedrooms_number > rooms_number:
            raise ValidationError('Numărul de dormitoare nu poate fi mai mare decât numărul total de camere.')

        floor = cleaned_data.get('floor')
        nr_floors = cleaned_data.get('nr_floors')

        if floor is not None and nr_floors is not None and floor > nr_floors:
            raise ValidationError('Numărul etajului apartamentului nu poate fi mai mare decât numărul total de etaje.')

        return cleaned_data


class HouseLeadCreateForm(ModelForm):
    class Meta:
        model = HouseLead
        fields = '__all__'
        widgets = {
            'house_type': SelectMultiple(attrs={'class': 'form-control'}),
            'destination': Select(attrs={'class': 'form-control'}),

            'rooms_number': NumberInput(attrs={'class': 'form-control'}),
            'nr_bedrooms': NumberInput(attrs={'class': 'form-control'}),
            'nr_kitchens': NumberInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': NumberInput(attrs={'class': 'form-control'}),
            'bathroom_window': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_floors': NumberInput(attrs={'class': 'form-control'}),

            'minimal_surface': NumberInput(attrs={'class': 'form-control'}),
            'terrain_surface': NumberInput(attrs={'class': 'form-control'}),
            'construction_status': SelectMultiple(attrs={'class': 'form-control'}),
            'furniture': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_finishes': SelectMultiple(attrs={'class': 'form-control'}),
            'construction_year': NumberInput(attrs={'class': 'form-control'}),

            'basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'attic': CheckboxInput(attrs={'class': 'form-check-input'}),
            'garage': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        rooms_number = cleaned_data.get('rooms_number')
        bedrooms_number = cleaned_data.get('nr_bedrooms')

        if bedrooms_number is not None and rooms_number is not None and bedrooms_number > rooms_number:
            raise ValidationError('Numărul de dormitoare nu poate fi mai mare decât numărul total de camere.')

        return cleaned_data


class TerrainLeadCreateForm(ModelForm):
    class Meta:
        model = TerrainLead
        fields = '__all__'
        widgets = {
            'terrain_type': Select(attrs={'class': 'form-control'}),
            'destination': Select(attrs={'class': 'form-control'}),
            'classification': Select(attrs={'class': 'form-control'}),

            'terrain_surface': NumberInput(attrs={'class': 'form-control'}),
            'unit': Select(attrs={'class': 'form-control'}),
            'street_front': NumberInput(attrs={'class': 'form-control'}),
            'opening_to': SelectMultiple(attrs={'class': 'form-control'}),
            'access_road_width': NumberInput(attrs={'class': 'form-control'}),

            'pot': TextInput(attrs={'class': 'form-control'}),
            'cut': TextInput(attrs={'class': 'form-control'}),
            'urban_certificate': CheckboxInput(attrs={'class': 'form-check-input'}),
            'building_permit': CheckboxInput(attrs={'class': 'form-check-input'}),
            'pug': CheckboxInput(attrs={'class': 'form-check-input'}),
            'puz': CheckboxInput(attrs={'class': 'form-check-input'}),
            'pud': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }


class CommercialSpaceLeadCreateForm(ModelForm):
    class Meta:
        model = CommercialSpaceLead
        fields = '__all__'
        widgets = {
            'space_type': SelectMultiple(attrs={'class': 'form-control'}),
            'destination': Select(attrs={'class': 'form-control'}),
            'pedestrian_traffic': SelectMultiple(attrs={'class': 'form-control'}),

            'rooms_number': NumberInput(attrs={'class': 'form-control'}),
            'nr_locker_rooms': NumberInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': NumberInput(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'nr_floors': NumberInput(attrs={'class': 'form-control'}),

            'minimal_surface': NumberInput(attrs={'class': 'form-control'}),
            'glass_case': NumberInput(attrs={'class': 'form-control'}),
            'inside_height': NumberInput(attrs={'class': 'form-control'}),
            'space_compart': SelectMultiple(attrs={'class': 'form-control'}),
            'nr_parking_spaces': NumberInput(attrs={'class': 'form-control'}),

            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        floor = cleaned_data.get('floor')
        nr_floors = cleaned_data.get('nr_floors')

        if floor is not None and nr_floors is not None and floor > nr_floors:
            raise ValidationError('Numărul etajului spațiului comercial nu poate fi mai mare decât numărul total de etaje.')

        return cleaned_data


class OfficeSpaceLeadCreateForm(ModelForm):
    class Meta:
        model = OfficeSpaceLead
        fields = '__all__'
        widgets = {
            'space_type': SelectMultiple(attrs={'class': 'form-control'}),
            'space_class': Select(attrs={'class': 'form-control'}),

            'rooms_number': NumberInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': NumberInput(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'nr_floors': NumberInput(attrs={'class': 'form-control'}),

            'useful_surface': NumberInput(attrs={'class': 'form-control'}),
            'minimum_area': NumberInput(attrs={'class': 'form-control'}),
            'maximum_area': NumberInput(attrs={'class': 'form-control'}),
            'total_surface_offices': NumberInput(attrs={'class': 'form-control'}),
            'space_compart': SelectMultiple(attrs={'class': 'form-control'}),

            'nr_underground_parking': NumberInput(attrs={'class': 'form-control'}),
            'underground_parking_cost': NumberInput(attrs={'class': 'form-control'}),
            'nr_surface_parking': NumberInput(attrs={'class': 'form-control'}),
            'surface_parking_cost': NumberInput(attrs={'class': 'form-control'}),

            'basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'elevator': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        minimum_area = cleaned_data.get('minimum_area')
        maximum_area = cleaned_data.get('maximum_area')

        if minimum_area is not None and maximum_area is not None and minimum_area >= maximum_area:
            raise ValidationError('Suprafața minimă nu poate fi mai mare sau egală cu suprafața maximă.')

        return cleaned_data


class IndustrialSpaceLeadCreateForm(ModelForm):
    class Meta:
        model = IndustrialSpaceLead
        fields = '__all__'
        widgets = {
            'space_type': SelectMultiple(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),

            'rooms_number': NumberInput(attrs={'class': 'form-control'}),
            'nr_locker_rooms': NumberInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': NumberInput(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),

            'minimal_surface': NumberInput(attrs={'class': 'form-control'}),
            'space_compart': SelectMultiple(attrs={'class': 'form-control'}),
            'terrain_surface': NumberInput(attrs={'class': 'form-control'}),
            'entrance_door_dimensions': TextInput(attrs={'class': 'form-control'}),
            'inside_height': NumberInput(attrs={'class': 'form-control'}),

            'powerline': CheckboxInput(attrs={'class': 'form-check-input'}),
            'truck_access': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }


########################################################################################################################
#                               ---   FORMULARE ACTUALIZARE   ---

class LeadUpdateForm(ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
        widgets = {
            'status': Select(attrs={'class': 'form-control'}),
            'property_type': TextInput(attrs={'readonly': 'readonly'}),
            'transaction_type': TextInput(attrs={'readonly': 'readonly'}),

            'contact': TextInput(attrs={'readonly': 'readonly'}),

            'county': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'zone': TextInput(attrs={'class': 'form-control'}),
            'street': TextInput(attrs={'class': 'form-control'}),

            'budget': TextInput(attrs={'class': 'form-control'}),
            'payment_method': Select(attrs={'class': 'form-control'}),

            'urgency': Select(attrs={'class': 'form-control'}),
            'other_details': Textarea(attrs={'readonly': 'readonly', 'rows': '3'}),

            'labels': Select(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control', 'rows': '3'}),

            'created_at': DateInput(attrs={'readonly': 'readonly'}),
            'updated_at': DateInput(attrs={'readonly': 'readonly'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()

        phone_number = cleaned_data.get('phone_number')
        email = cleaned_data.get('email')
        errors = {}

        if not phone_number and not email:
            errors[
                'phone_number'] = 'Trebuie să introduci obligatoriu un număr de telefon sau o adresă de e-mail pentru contact.'

        if phone_number:
            lead_id = self.instance.id
            check_phone_number = Lead.objects.filter(phone_number=phone_number).exclude(id=lead_id)
            if check_phone_number.exists():
                msg = f'''Există deja un contact cu acest număr de telefon. 
                Introdu alt număr de telefon sau actualizează contactul deja existent.'''
                errors['phone_number'] = msg

        if email:
            lead_id = self.instance.id
            check_email = Lead.objects.filter(email=email).exclude(id=lead_id)
            if check_email.exists():
                msg = f'''Există deja un contact cu această adresă de e-mail. 
                Introdu altă adresă de e-mail sau actualizează contactul deja existent.'''
                errors['email'] = msg

        if errors:
            raise ValidationError(errors)

        return cleaned_data


class ApartmentLeadUpdateForm(ModelForm):
    class Meta:
        model = ApartmentLead
        fields = '__all__'
        widgets = {
            'apartment_type': SelectMultiple(attrs={'class': 'form-control'}),
            'destination': Select(attrs={'class': 'form-control'}),

            'rooms_number': NumberInput(attrs={'class': 'form-control'}),
            'nr_bedrooms': NumberInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': NumberInput(attrs={'class': 'form-control'}),
            'bathroom_window': CheckboxInput(attrs={'class': 'form-check-input'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'excluded_ground_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'excluding_top_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_floors': NumberInput(attrs={'class': 'form-control'}),

            'minimal_surface': NumberInput(attrs={'class': 'form-control'}),
            'construction_status': SelectMultiple(attrs={'class': 'form-control'}),
            'furniture': SelectMultiple(attrs={'class': 'form-control'}),
            'comfort': SelectMultiple(attrs={'class': 'form-control'}),
            'ap_compart': SelectMultiple(attrs={'class': 'form-control'}),
            'orientation': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_finishes': SelectMultiple(attrs={'class': 'form-control'}),
            'construction_year': NumberInput(attrs={'class': 'form-control'}),

            'basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'attic': CheckboxInput(attrs={'class': 'form-check-input'}),
            'elevator': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        rooms_number = cleaned_data.get('rooms_number')
        bedrooms_number = cleaned_data.get('nr_bedrooms')

        if bedrooms_number is not None and rooms_number is not None and bedrooms_number > rooms_number:
            raise ValidationError('Numărul de dormitoare nu poate fi mai mare decât numărul total de camere.')

        floor = cleaned_data.get('floor')
        nr_floors = cleaned_data.get('nr_floors')

        if floor is not None and nr_floors is not None and floor > nr_floors:
            raise ValidationError('Numărul etajului apartamentului nu poate fi mai mare decât numărul total de etaje.')

        return cleaned_data


class HouseLeadUpdateForm(ModelForm):
    class Meta:
        model = HouseLead
        fields = '__all__'
        widgets = {
            'house_type': SelectMultiple(attrs={'class': 'form-control'}),
            'destination': Select(attrs={'class': 'form-control'}),

            'rooms_number': NumberInput(attrs={'class': 'form-control'}),
            'nr_bedrooms': NumberInput(attrs={'class': 'form-control'}),
            'nr_kitchens': NumberInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': NumberInput(attrs={'class': 'form-control'}),
            'bathroom_window': CheckboxInput(attrs={'class': 'form-check-input'}),
            'nr_floors': NumberInput(attrs={'class': 'form-control'}),

            'minimal_surface': NumberInput(attrs={'class': 'form-control'}),
            'terrain_surface': NumberInput(attrs={'class': 'form-control'}),
            'construction_status': SelectMultiple(attrs={'class': 'form-control'}),
            'furniture': SelectMultiple(attrs={'class': 'form-control'}),
            'interior_finishes': SelectMultiple(attrs={'class': 'form-control'}),
            'construction_year': NumberInput(attrs={'class': 'form-control'}),

            'basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'attic': CheckboxInput(attrs={'class': 'form-check-input'}),
            'garage': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        rooms_number = cleaned_data.get('rooms_number')
        bedrooms_number = cleaned_data.get('nr_bedrooms')

        if bedrooms_number is not None and rooms_number is not None and bedrooms_number > rooms_number:
            raise ValidationError('Numărul de dormitoare nu poate fi mai mare decât numărul total de camere.')

        return cleaned_data


class TerrainLeadUpdateForm(ModelForm):
    class Meta:
        model = TerrainLead
        fields = '__all__'
        widgets = {
            'terrain_type': Select(attrs={'class': 'form-control'}),
            'destination': Select(attrs={'class': 'form-control'}),
            'classification': Select(attrs={'class': 'form-control'}),

            'terrain_surface': NumberInput(attrs={'class': 'form-control'}),
            'unit': Select(attrs={'class': 'form-control'}),
            'street_front': NumberInput(attrs={'class': 'form-control'}),
            'opening_to': SelectMultiple(attrs={'class': 'form-control'}),
            'access_road_width': NumberInput(attrs={'class': 'form-control'}),

            'pot': TextInput(attrs={'class': 'form-control'}),
            'cut': TextInput(attrs={'class': 'form-control'}),
            'urban_certificate': CheckboxInput(attrs={'class': 'form-check-input'}),
            'building_permit': CheckboxInput(attrs={'class': 'form-check-input'}),
            'pug': CheckboxInput(attrs={'class': 'form-check-input'}),
            'puz': CheckboxInput(attrs={'class': 'form-check-input'}),
            'pud': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }


class CommercialSpaceLeadUpdateForm(ModelForm):
    class Meta:
        model = CommercialSpaceLead
        fields = '__all__'
        widgets = {
            'space_type': SelectMultiple(attrs={'class': 'form-control'}),
            'destination': Select(attrs={'class': 'form-control'}),
            'pedestrian_traffic': SelectMultiple(attrs={'class': 'form-control'}),

            'rooms_number': NumberInput(attrs={'class': 'form-control'}),
            'nr_locker_rooms': NumberInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': NumberInput(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'nr_floors': NumberInput(attrs={'class': 'form-control'}),

            'minimal_surface': NumberInput(attrs={'class': 'form-control'}),
            'glass_case': NumberInput(attrs={'class': 'form-control'}),
            'inside_height': NumberInput(attrs={'class': 'form-control'}),
            'space_compart': SelectMultiple(attrs={'class': 'form-control'}),
            'nr_parking_spaces': NumberInput(attrs={'class': 'form-control'}),

            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        floor = cleaned_data.get('floor')
        nr_floors = cleaned_data.get('nr_floors')

        if floor is not None and nr_floors is not None and floor > nr_floors:
            raise ValidationError('Numărul etajului spațiului comercial nu poate fi mai mare decât numărul total de etaje.')

        return cleaned_data


class OfficeSpaceLeadUpdateForm(ModelForm):
    class Meta:
        model = OfficeSpaceLead
        fields = '__all__'
        widgets = {
            'space_type': SelectMultiple(attrs={'class': 'form-control'}),
            'space_class': Select(attrs={'class': 'form-control'}),

            'rooms_number': NumberInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': NumberInput(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),
            'nr_floors': NumberInput(attrs={'class': 'form-control'}),

            'useful_surface': NumberInput(attrs={'class': 'form-control'}),
            'minimum_area': NumberInput(attrs={'class': 'form-control'}),
            'maximum_area': NumberInput(attrs={'class': 'form-control'}),
            'total_surface_offices': NumberInput(attrs={'class': 'form-control'}),
            'space_compart': SelectMultiple(attrs={'class': 'form-control'}),

            'nr_underground_parking': NumberInput(attrs={'class': 'form-control'}),
            'underground_parking_cost': NumberInput(attrs={'class': 'form-control'}),
            'nr_surface_parking': NumberInput(attrs={'class': 'form-control'}),
            'surface_parking_cost': NumberInput(attrs={'class': 'form-control'}),

            'basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'semi_basement': CheckboxInput(attrs={'class': 'form-check-input'}),
            'technical_floor': CheckboxInput(attrs={'class': 'form-check-input'}),
            'loft': CheckboxInput(attrs={'class': 'form-check-input'}),
            'elevator': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        minimum_area = cleaned_data.get('minimum_area')
        maximum_area = cleaned_data.get('maximum_area')

        if minimum_area is not None and maximum_area is not None and minimum_area >= maximum_area:
            raise ValidationError('Suprafața minimă nu poate fi mai mare sau egală cu suprafața maximă.')

        return cleaned_data


class IndustrialSpaceLeadUpdateForm(ModelForm):
    class Meta:
        model = IndustrialSpaceLead
        fields = '__all__'
        widgets = {
            'space_type': SelectMultiple(attrs={'class': 'form-control'}),
            'destination': SelectMultiple(attrs={'class': 'form-control'}),

            'rooms_number': NumberInput(attrs={'class': 'form-control'}),
            'nr_locker_rooms': NumberInput(attrs={'class': 'form-control'}),
            'nr_bathrooms': NumberInput(attrs={'class': 'form-control'}),
            'floor': SelectMultiple(attrs={'class': 'form-control'}),

            'minimal_surface': NumberInput(attrs={'class': 'form-control'}),
            'space_compart': SelectMultiple(attrs={'class': 'form-control'}),
            'terrain_surface': NumberInput(attrs={'class': 'form-control'}),
            'entrance_door_dimensions': TextInput(attrs={'class': 'form-control'}),
            'inside_height': NumberInput(attrs={'class': 'form-control'}),

            'powerline': CheckboxInput(attrs={'class': 'form-check-input'}),
            'truck_access': CheckboxInput(attrs={'class': 'form-check-input'}),

            'assigned_listings': TextInput(attrs={'class': 'form-control'}),
        }
