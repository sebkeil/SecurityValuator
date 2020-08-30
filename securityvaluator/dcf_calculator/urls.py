from django.urls import path
from . import views

#app_name = 'dcf_calculator' #change this in models > reverse (for dynamic routing)
urlpatterns = [
    path('', views.dcf_index_view, name='dcf_index'),
    path('dcf_results', views.dcf_results_view, name='dcf_results'),
    path('enterprise_database', views.enterprise_database_view, name='enterprise_database'),
    #path('stock_database/<int:id>', views.individual_stock_view, name='individual_stock')
    path('enterprise_database/<int:id>', views.dynamic_lookup_view, name='enterprise'),
    path('enterprise_database/<int:id>/delete', views.enterprise_delete_view, name='enterprise_delete')
]

