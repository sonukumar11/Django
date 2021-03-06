from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import City

class CityForm(forms.ModelForm):
    

    class Meta:
        model = City
        fields = ('city_name',)
        widgets = {
            'city_name' : forms.TextInput(attrs={'class':'form-control my-3 city-input w-75 mx-auto','placeholder':'Enter Your City Name'})
        }