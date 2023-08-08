from django.contrib import admin
from .models import Producto, Precio_stock

# Register your models here.


class PreciosInLine(admin.TabularInline):
    model = Precio_stock
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    # ... other configurations ...

    def get_precios(self, obj):
        precios = obj.precios.all()
        return ", ".join(str(p.precio) for p in precios) if precios.exists() else None

    # Define descripciones personalizadas para las columnas
    get_precios.short_description = "Precios"

    # Utiliza los métodos en list_display
    list_display = ("name", "get_precios",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [PreciosInLine]

admin.site.register(Producto, ProductoAdmin)