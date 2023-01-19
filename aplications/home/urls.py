from django.urls import path
from . import views
urlpatterns = [
    path("home/", views.IndexView.as_view(), name = "home"),
    path("lista/", views.PruebaListView.as_view(), name = "Lista Prueba"),
    path("prueba/", views.ModeloListView.as_view(), name = "prueba"),
    path("createPrueba/", views.PruebaCreateView.as_view(), name= "CreatePrueba")
]