from django.urls import path
from . import views

urlpatterns = [
    path('', views.dcf_index, name='dcf_index'),
    path('make_dcf_calculation/', views.make_dcf_calculations, name="make_dcf_calculation"),
    path('make_dcf_calculation_alt', views.make_dcf_calculations_alt, name='make_dcf_calculation_alt'),
    path('create_enterprise/', views.create_enterprise_view, name='create_enterprise')
]

