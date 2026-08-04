from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('aboutUs/',views.aboutUs,name='aboutUs'),
    path('loginPage/',views.loginPage,name = 'loginPage')
]

# http://localhost:8000
# home