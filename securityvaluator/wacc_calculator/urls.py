from django.urls import path
from . import views

urlpatterns = [
    path('', views.wacc_index_view, name='wacc_index'),
    path('wacc_results', views.wacc_results_view, name='wacc_results')
]

