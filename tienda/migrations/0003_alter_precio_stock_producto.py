# Generated by Django 4.2.4 on 2023-08-03 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_precio_stock_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precio_stock',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='precio', to='tienda.producto'),
        ),
    ]
