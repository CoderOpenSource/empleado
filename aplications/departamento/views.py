from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Departamento
from aplications.empleados.models import Empleado
# Create your views here.

class NewDepartamentoView(FormView):
    template_name = "departamentos/new_departamento.html"
    form_class = NewDepartamentoForm
    success_url = reverse_lazy("departamento_app:ListDepartamento")

    def form_valid(self, form):
        print("********Estamos en el form valid********")

        departamento = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        departamento.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name= nombre,
            last_name = apellido,
            job = '1',
            id_departamento = departamento
        )

        return super(NewDepartamentoView, self).form_valid(form)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamentos/list_all.html"
    context_object_name = "departamentos"