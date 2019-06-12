from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from django.shortcuts import render, redirect

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import requests
from django.forms import ModelForm, TextInput
from .models import City,graph

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder



class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
    def clean_email(self):
            # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')

class Inputdata(ModelForm):
    Date=forms.CharField(widget = forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model=graph
    
        fields=['city','Date','Temp']

        