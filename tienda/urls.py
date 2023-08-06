from django.urls import path
from .views import PrincipalView, CategoriasView, ProductoDetailView

app_name = "tienda"

urlpatterns = [
    path('', PrincipalView.as_view(), name="home"),
    path('productos/', CategoriasView.as_view(), name='listado'),
    path('productos/<slug:slug>/', ProductoDetailView.as_view(), name='detalle'),

]