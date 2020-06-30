from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate_wacc', views.calculate_wacc, name='calculate_wacc')
]

