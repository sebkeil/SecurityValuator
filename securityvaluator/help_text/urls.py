from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_help, name='main_help')
]