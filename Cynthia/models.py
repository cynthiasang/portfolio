from email import message
from django.db import models
from email.message import Message
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.forms import NullBooleanField
# Create your models here.

class Guest(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    status= models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    profile =  models.ImageField(upload_to ='images',blank=True,null=True,help_text='upload image size less than 2.0MB')
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class About(models.Model):

    date=models.DateField(auto_now=True)
    image = models.ImageField(null=True,upload_to='media_cdn/images/%Y/%m/%d')
    by=models.CharField(max_length=20,null=True,default='Cynthia')
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.message


class Service(models.Model):
    
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    
class Skill(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    type = models.CharField(max_length=100)
    percentage = models.CharField(max_length=20)


class ContactusForm(models.Model):
    email = models.EmailField(max_length=100)
    namesender = models.CharField(max_length=70)
    message = models.CharField(max_length=200) 
    


class Contact(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    emailowner = models.CharField(max_length=80)
    para = models.TextField(max_length=200) 
