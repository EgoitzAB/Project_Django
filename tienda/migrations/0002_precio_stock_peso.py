# Generated by Django 4.2.4 on 2023-08-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='precio_stock',
            name='peso',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
