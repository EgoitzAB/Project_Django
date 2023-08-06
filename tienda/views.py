from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from tienda.models import Producto
from tienda.forms import ProductoModelForm
from django.conf import settings

# Create your views here.

class PrincipalView(View):
    def get(self, request, *args, **kwargs):
        productos = Producto.objects.filter(active=True)
        form = ProductoModelForm()

        digital_products_data = None

        if productos:
            paginator = Paginator(productos, 3)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)
        
        context={
            'products':digital_products_data,
            'form':form
        }
        return render(request, 'tienda/index.html', context)
    
    def post(self, request, *args, **kwargs):
        productos = Producto.objects.filter(active=True)

        form=ProductoModelForm()

        if request.method == "POST":
            form=ProductoModelForm(request.POST, request.FILES)

            if form.is_valid():
                form.user=request.user
                form.save()
                return redirect('home')
            
        digital_products_data = None

        if productos:
            paginator = Paginator(productos, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)
        
        context={
            'products':digital_products_data
        }
        return render(request, 'tienda/index.html', context)
    
class CategoriasView(ListView):
    model = Producto
    template_name = 'tienda/listado.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context


