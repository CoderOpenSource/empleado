from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Empleado
from django.urls import reverse_lazy
#forms
from .forms import EmpleadoForm
# Create your views here.
class InicioView(TemplateView):
    template_name = "inicio.html"

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    context_object_name = "empleados"
    paginate_by = 3
    ordering = "first_name"
    def get_queryset(self):
        buscar = self.request.GET.get("busqueda", '')
        lista = Empleado.objects.filter(
            full_name__icontains = buscar
        )

        return lista
    def get_context_data(self, **kwargs):
        buscar = self.request.GET.get("busqueda", '')
        context = super(ListAllEmpleados, self).get_context_data(**kwargs)
        context['buscar'] = buscar
        print(buscar)
        return context


class ListarPorArea(ListView):
    model = Empleado
    template_name = 'persona/listarArea.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        shorname = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            id_departamento__shor_name = shorname
        )
        return lista
    def get_context_data(self, **kwargs):
        buscar = self.kwargs['shorname']
        context = super(ListarPorArea, self).get_context_data(**kwargs)
        context['shorname'] = buscar
        print(buscar)
        return context


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = "Empleado destacado"
        return context

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/create_empleado.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy("persona_app:listaAdminEmpleados")
    def form_valid(self, form):
        empleado = form.save(commit = False)
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update-empleado.html"
    fields = (
        "first_name",
        "last_name",
        "job",
        "id_departamento",
        "avatar",
        "id_habilidad"
    )
    success_url = reverse_lazy("persona_app:listaAdminEmpleados")

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete-empleado.html"
    success_url = reverse_lazy("persona_app:listaAdminEmpleados")

# administrarEmpleados
class ListarEmpleadosAdmin(ListView):
    template_name = 'persona/listar_admin_empleados.html'
    context_object_name = "empleados"
    paginate_by = 10
    ordering = "last_name"
    model = Empleado