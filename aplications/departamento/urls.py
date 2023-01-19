from django.contrib import admin
from django.urls import path
from .views import NewDepartamentoView
from .views import *
app_name = "departamento_app"
urlpatterns = [
    path("NewDepartamento/", NewDepartamentoView.as_view(), name ="NewDepartamento")
    , path("list_all", DepartamentoListView.as_view(), name = "ListDepartamento")
]
