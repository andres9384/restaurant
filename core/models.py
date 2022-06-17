from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Ingredient(models.Model):
    """Modelo Ingrediente"""
    name = models.CharField(max_length=30, verbose_name="Nombre")
    price = models.DecimalField(validators=[MinValueValidator(0.00)], default=0.00, decimal_places=2, max_digits=9, verbose_name="Precio")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'


class Pizza(models.Model):
    """Modelo Pizza"""
    ingredient = models.ManyToManyField(Ingredient)
    name = models.CharField(max_length=45, verbose_name="Nombre")
    size = models.CharField(default="Normal", max_length=30, verbose_name="Tamaño")
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=9, verbose_name="Precio")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'

