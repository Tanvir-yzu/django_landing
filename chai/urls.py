from django.urls import path
from . import views

urlpatterns = [
    path('', views.al_chai, name='al_chai'),
]