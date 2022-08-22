from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('search-drug/', views.search_drug, name='search-drug'),

]