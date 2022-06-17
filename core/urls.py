# DJANGO
from django.urls import path
# VIEWS
#from core.views import index
from .views import *


urlpatterns = [
    #Ruta normal
    #path('index', index, name="index"),

    #Url con parametros
   # path('<str:parametro>/', index, name="index"),
    path('pizzas/', Listpizza.as_view(), name="listPizza"),
]
