from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PruebaForm
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
# Create your views here.
class IndexView(TemplateView):
    template_name = "home/home.html"

class PruebaListView(ListView):
    template_name = "home/lista.html"
    model = Prueba
    context_object_name = "pruebas"

class ModeloListView(ListView):
    template_name = "home/prueba.html"
    model = Prueba
    context_object_name = "Pruebas"

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/createPrueba.html"
    form_class = PruebaForm
    success_url = reverse_lazy("Lista Prueba")