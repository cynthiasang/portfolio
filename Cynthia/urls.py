from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views    
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static


urlpatterns = [
     path('',views.home_view,name='home'),
     path('about/view/',views.about_view,name='about'),
     path('services/view/all/',views.services_view,name='services'),
     path('skills/view/',views.skills_view,name='skills'),
     path('contact',views.contact_view,name='contact'),
     
]