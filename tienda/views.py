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
from django.http import FileResponse
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
# Create your views here.


class PrincipalView(View):
    def get(self, request):
        productos = Producto.objects.filter(active=True).order_by('categoria')
        
        categorias_con_productos = {}
        for producto in productos:
            if producto.categoria not in categorias_con_productos:
                categorias_con_productos[producto.categoria] = []
            categorias_con_productos[producto.categoria].append(producto)
        
        context = {
            'categorias_con_productos': categorias_con_productos,
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

@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon(request):
    file = (settings.BASE_DIR / "static" / "favicon.ico").open("rb")
    return FileResponse(file)


