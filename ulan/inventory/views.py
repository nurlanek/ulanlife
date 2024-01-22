# inventory/views.py
from django.shortcuts import render, redirect
from .models import Material, MaterialTransaction

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'inventory/material_list.html', {'materials': materials})

def material_transaction(request, material_id):
    if request.method == 'POST':
        quantity_change = int(request.POST.get('quantity_change'))
        material = Material.objects.get(pk=material_id)
        MaterialTransaction.objects.create(material=material, quantity_change=quantity_change)
        material.quantity += quantity_change
        material.save()
    return redirect('material_list')

def inventory_summary(request):
    materials = Material.objects.all()
    return render(request, 'inventory/inventory_summary.html', {'materials': materials})
