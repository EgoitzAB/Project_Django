from django.urls import path
from .views import create_checkout_session, carrito, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito
from django.conf import settings
import stripe

app_name = "compra"

urlpatterns = [
        path('create-checkout-session/', create_checkout_session, name="create-checkout-session"),
        path('carrito/', carrito, name="carrito"),
        path('agregar/', agregar_producto, name="agregar"),
        path('eliminar/<int:producto_id>/', eliminar_producto, name="eliminar"),
        path('restar/<int:producto_id>/', restar_producto, name="restar"),
        path('limpiar/', limpiar_carrito, name="limpiar"),
]