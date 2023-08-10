# forms.py
from django import forms
from .models import UserProfile

class TaxiDriverForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['is_taxi_driver']
        
class phoneNumberForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number']
