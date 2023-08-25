from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from tienda.models import Producto
from tienda.forms import ProductoModelForm
from django.conf import settings
from compra.context_processor import carrito_total

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
    
    
class CategoriasView(ListView):
    model = Producto
    template_name = 'tienda/listado.html'
    context_object_name = 'productos'  # Nombre con el que se accederá a los productos en el template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener la categoría seleccionada de la URL
        categoria_seleccionada = self.request.GET.get('categoria')

        # Filtrar productos por categoría si se seleccionó una
        if categoria_seleccionada:
            context['categoria_seleccionada'] = categoria_seleccionada
            context['productos'] = Producto.objects.filter(categoria=categoria_seleccionada)

        return context

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'tienda/detalle.html'


