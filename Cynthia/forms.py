from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
from . models import  About


#signup form

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


	   

class GuestForm(forms.ModelForm):
    class Meta:
        model=models.Guest
        fields=['name','status']      


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

         
class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = '__all__'

   
    
    