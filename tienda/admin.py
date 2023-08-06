from django.contrib import admin
from .models import Producto, Precio_stock

# Register your models here.


class PreciosInLine(admin.TabularInline):
    model = Precio_stock

class ProductoAdmin(admin.ModelAdmin):
    # ... other configurations ...

    def get_precios(self, obj):
        precios = obj.precios.all()
        return precios if precios.exists() else None

    # Define descripciones personalizadas para las columnas
    get_precios.short_description = "Precios"

    # Utiliza los métodos en list_display
    list_display = ("name", "get_precios",)  # Use "name" or other valid fields of the Producto model
    prepopulated_fields = {"slug": ("name",)}
    inlines = [PreciosInLine]

admin.site.register(Producto, ProductoAdmin)
