from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.election,name='election'),
    path('contactUs/',views.contactUs,name='contactUs'),
    path('Register/',views.Register,name = 'Register')
]