from django.urls import path
from salonAapp import views

urlpatterns = [
    path('', views.home, name='home'),


]