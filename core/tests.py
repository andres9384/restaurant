from django.test import TestCase
from pizzeria.wsgi import *
from core.models import Ingredient


# Create your tests here.
new = Ingredient()
new.name = "Salami"
new.price = "8000"
new.save()
query = Ingredient.objects.all()
print(query)
