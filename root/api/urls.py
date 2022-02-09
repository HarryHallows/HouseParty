from django.urls import path
from .views import RoomView

# URLS Locally to this app

urlpatterns = [
    path('room', RoomView.as_view())  # if we get a blank url then return to main/home
]
