from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from core.models import *

# Create your views here.

"""
def index(request, parametro):
    data = {
        'parametros': parametro,
        'ingredientes': Ingredient.objects.all()}
    return render(request, 'core/pizzas.html', data)
"""

class Listpizza(ListView):
    """Lista de todos las pizzas """
    model = Ingredient
    template_name = 'core/pizzas.html'



