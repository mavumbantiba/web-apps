from django.db import models
from django_countries.fields import *
from phonenumber_field.modelfields import *
# Create your models here.

class PersonalInformation(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10, choices={
        'MALE':'MALE',
        'FEMALE':'FEMALE'
    })
    country=CountryField()
    email=models.EmailField(unique=True)
    phone=PhoneNumberField()

    class Meta:
        ordering=['name']
        unique_together=['country','phone']


    def __str__(self):
        return f'{self.name}'