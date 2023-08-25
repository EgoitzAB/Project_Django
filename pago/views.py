from django.shortcuts import render, HttpResponse

# Create your views here.
import Monei
from Monei import ApiException, CreatePaymentRequest
from pprint import pprint

# Instantiate the client using the API key

def crear_cliente(request):
    monei = Monei.MoneiClient(api_key="pk_test_36cf3e8a15eff3f5be983562ea6b13ec")
    try:
        # Create Payment
        result = monei.payments.create({
            'amount': 1250, # 12.50€
            'orderId': '100200000001',
            'currency': 'EUR',
            'description': 'Items description',
            'customer': {
                'email': 'john.doe@monei.com',
                'name': 'John Doe'
            }
        })
        return HttpResponse(result)
    except ApiException as e:
        return HttpResponse("Error while creating payment: %s\n" % e)

def crear_pago(request):
    monei = Monei.MoneiClient(api_key="pk_test_36cf3e8a15eff3f5be983562ea6b13ec")
    monei.Payments.create(CreatePaymentRequest(
        amount=110,
        currency="EUR",
        order_id="14379133960355",
        payment_token="7cc38b08ff471ccd313ad62b23b9f362b107560b",
        callback_url="/",
        complete_url="/"
    ))
