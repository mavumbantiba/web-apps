from django.shortcuts import render, redirect
from django.contrib.auth.decorators import *
from .models import *
from .forms import *
from django.contrib import messages
from sudo.decorators import sudo_required
from django.contrib.auth.models import User

@login_required
# @sudo_required
def homepage_view(request):
    return render(request,'templates/homepage.html')

# @sudo_required
@login_required
def register_person_view(request):
    people=PersonalInformation.objects.all()
    form=PersonalInformationRegistrationForm()
    if request.method=='POST':
        form=PersonalInformationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'{form.instance.name} has been registed successfull...!')
            return redirect('register')
    return render(request,'templates/register-person.html',{'form':form,'people':people})

@login_required
# @sudo_required
def list_view(request):
    people=PersonalInformation.objects.all()
    return render(request,'templates/list.html',{'people':people})

@login_required
def manage_account(request):
    return render(request,'templates/manage-account.html')

@login_required
def delete_account(request):
    users=User.objects.all()
    user=request.user
    if request.user:
        user.delete()
        messages.success(request, f'User {request.user.username} has been deleted successfuly..............!')
    elif request.user.is_superuser:
        users.delete
        messages.success(request, f'All users have been deleted successfuly..............!')
    else:
        messages.info(request,'Access denied. You do not have enough privileges to perfome this action')
    return redirect('home')
    