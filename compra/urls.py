from django.urls import path
from .views import create_checkout_session
from django.conf import settings
import stripe

app_name = "compra"

urlpatterns = [
        path('create-checkout-session/', create_checkout_session, name="create-checkout-session"),
]