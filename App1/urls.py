from django.urls import path
from App1.views import *
urlpatterns = [
    path('',homepage_view,name='home'),
    path('register-person',register_person_view,name='register'),
    path('registered',list_view,name='registered'),    
    path('manage-account',manage_account,name='manage-account'),
    path('delete-account',delete_account,name='delete-account')

]
