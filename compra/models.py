from django.db import models
from tienda.models import Producto

# Create your models here.
class ProductoComprado(models.Model):
    email = models.EmailField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email