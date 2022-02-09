from django.urls import path
from .views import main

# URLS Locally to this app

urlpatterns = [
    path('', main)  # if we get a blank url then return to main/home
]
