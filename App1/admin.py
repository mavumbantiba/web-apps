from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(PersonalInformation)
class PersonalInformationDisplay(admin.ModelAdmin):
    list_display=('name','gender','country','phone','email')
    list_filter=('name','gender','country','phone')
    search_fields=('name','gender','coountry','phone','email')