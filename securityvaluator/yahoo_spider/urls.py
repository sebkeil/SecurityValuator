from django.urls import path
from . import views

urlpatterns = [
    path('', views.yahoo_spider_index_view, name= 'yahoo_spider_index'),
    path('yahoo_spider_balance_sheet', views.yahoo_spider_balance_sheet_view, name='yahoo_spider_balance_sheet')
]
