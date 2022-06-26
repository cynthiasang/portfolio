from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import About, Skill, Guest, Service, Contact
from django.contrib import admin




#register your models here
admin.site.register(Guest)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(About)
admin.site.register(Contact)










