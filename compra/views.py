from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from tienda.models import Producto, Precio_stock
from django.http.response import JsonResponse
from django.urls import reverse
from django.conf import settings
from compra.carrito import Carrito
import stripe

# Create your views here.
def create_checkout_session(request, *args, **kwargs):
    product_id = request.POST.get("product_id")
    precio = get_object_or_404(Precio_stock, id=product_id)
    product = precio.producto

    domain = "https://egoitzabilleira.es"
    if settings.DEBUG:
        domain = "http://127.0.0.1:8000"

    customer = None
    customer_email = None

    if request.user.is_authenticated:
        if request.user.stripe_customer_id:
            customer = request.user.stripe_customer_id
        else:
            customer_email = request.user.email

        # Convert the product price to cents
    unit_amount_in_cents = int(precio.precio * 100)

    session = stripe.checkout.Session.create(
        customer=customer,
        customer_email=customer_email,
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': unit_amount_in_cents,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=domain + reverse("success"),
        cancel_url=domain + reverse("home"),
        metadata={
            "product_id": product.id
        }
    )

    return JsonResponse({
        "id": session.id
    })

def carrito(request):
    carrito = Carrito(request)
    return render(request, "compra/carrito.html", {"carrito": carrito})



def agregar_producto(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        carrito = Carrito(request)
        producto = Precio_stock.objects.get(id=producto_id)
        carrito.agregar(producto)
        return redirect("compra:carrito")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Precio_stock.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("compra:carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Precio_stock.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("compra:carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("compra:carrito")

