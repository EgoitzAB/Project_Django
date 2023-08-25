from django.urls import path
from .views import crear_pago, crear_cliente
from django.conf import settings

app_name = "pago"

urlpatterns = [
        path('crear-pago/', crear_pago, name="crear-pago"),
        path('crear-cliente/', crear_cliente, name='crear-cliente'),
    ]