from django.forms import *
from django import forms
from phonenumber_field.formfields import *
from phonenumber_field.widgets import *
from .models import *

class PersonalInformationRegistrationForm(forms.ModelForm):
    phone=SplitPhoneNumberField(initial=['TZ',])

    class Meta:
        model=PersonalInformation
        fields='__all__'
        