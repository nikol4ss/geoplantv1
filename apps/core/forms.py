from django import forms
from .models import BotanicalRegister

class BotanicalForm(forms.ModelForm):
    class Meta:
        model = BotanicalRegister
        fields = '__all__'

    widgets = {
            'binomial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome binomial'}),
            'common_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome comum'}),
            'botanical_family': forms.TextInput(attrs={'class': 'form-control'}),
            'genus': forms.TextInput(attrs={'class': 'form-control'}),
            'species': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),

            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'diameter': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'stem_type': forms.Select(attrs={'class': 'form-control'}),
            'leaf_type': forms.Select(attrs={'class': 'form-control'}),
            'flower_type': forms.Select(attrs={'class': 'form-control'}),
            'flowering_period': forms.Select(attrs={'class': 'form-control'}),
            'fruit_type': forms.Select(attrs={'class': 'form-control'}),
            'fruiting_period': forms.Select(attrs={'class': 'form-control'}),
            'morphological_observations': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),

            'soil_type': forms.Select(attrs={'class': 'form-control'}),
            'soil_pH': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'moisture': forms.Select(attrs={'class': 'form-control'}),
            'lighting': forms.Select(attrs={'class': 'form-control'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'climate': forms.Select(attrs={'class': 'form-control'}),

            'water_requirement': forms.Select(attrs={'class': 'form-control'}),
            'watering_frequency': forms.Select(attrs={'class': 'form-control'}),
            'fertilization_type': forms.Select(attrs={'class': 'form-control'}),

            'susceptibility': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cultivation_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),

            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'state_province': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'specific_location': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'altitude_meters': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'biome': forms.TextInput(attrs={'class': 'form-control'}),
            'ecosystem': forms.TextInput(attrs={'class': 'form-control'}),

            'registration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'planting_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'collection_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'origin': forms.TextInput(attrs={'class': 'form-control'}),
            'collection_number': forms.TextInput(attrs={'class': 'form-control'}),
            'registered_by': forms.TextInput(attrs={'class': 'form-control'}),

            'general_image': forms.ImageField(),
            'stem_image': forms.ImageField(),
            'leaf_image': forms.ImageField(),
            'flower_image': forms.ImageField(),
            'fruit_image': forms.ImageField()
        }
