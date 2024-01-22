# inventory/urls.py
from django.urls import path
from .views import material_list, material_transaction, inventory_summary

urlpatterns = [
    path('materials/', material_list, name='material_list'),
    path('material/<int:material_id>/transaction/', material_transaction, name='material_transaction'),
    path('inventory/summary/', inventory_summary, name='inventory_summary'),
]
