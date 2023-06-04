from django.contrib import admin
from django.urls import path, include
from CharityApp import views

urlpatterns = [
    path('orgsignup/', views.orgsignup, name="orgsignup"),
    path('get_token/', views.get_token, name='get_token'),
    path('organizations/', views.organizations, name='organizations'),
]
