from django.urls import path
from . import views

urlpatterns = [
    path('', views.dcf_index_view, name='dcf_index'),
    path('dcf_results', views.dcf_results_view, name='dcf_results'),
    path('create_enterprise/', views.create_enterprise_view, name='create_enterprise')
]

