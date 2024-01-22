from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Order

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'