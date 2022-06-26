from django.shortcuts import render
from multiprocessing import context
from django.contrib.auth.forms import UsernameField
from django.shortcuts import render
from django.shortcuts import reverse,render,redirect,get_object_or_404
from . import forms,models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.core.mail import send_mail
from Cynthia import models as MMODEL
from .models import Contact, Service
from .models import Skill, About
from django.contrib.auth import authenticate, login, logout
from .forms import  ContactusForm, CreateUserForm, AboutForm
import uuid


# Create your views here.

def home_view(request):
    return render (request, 'folio/index.html')

def about_view(request):

    about = About.objects.all()
    context = {'about':about}
    return render (request, 'folio/about.html', context)  

def skills_view(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render (request, 'folio/skills.html', context)

def services_view(request):
    a = Service.objects.all()
    context = {'a': a}
    return render (request, 'folio/services.html', context)

def contact(request):
    contacts = Contact.oblects.all()
    context = {'contacts': contacts}
    return render (request, 'folio/contact.html', context)


def contact_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'folio/index.html')
    return render(request, 'folio/contact.html', {'form':sub})    

                     