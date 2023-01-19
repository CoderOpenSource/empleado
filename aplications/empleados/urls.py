from django.urls import path
from . import views
app_name = "persona_app"
urlpatterns = [
    path('', views.InicioView.as_view(), name = "inicio"),
    path('listar-empleados', views.ListAllEmpleados.as_view(), name = "listaEmpleados"),
    path('listar-by-area/<shorname>/', views.ListarPorArea.as_view(), name = "listarAreaEmpleados"),
    path('detail-empleado/<pk>', views.EmpleadoDetailView.as_view(), name = "DetalleEmpleado"),
    path('create-empleado/', views.EmpleadoCreateView.as_view(), name ="CreateEmpleado"),
    path('update-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name="UpdateEmpleado"),
    path('delete-empleado/<pk>', views.EmpleadoDeleteView.as_view(), name = "DeleteEmpleado")
    ,    path('listar-empleados-admin', views.ListarEmpleadosAdmin.as_view(), name = "listaAdminEmpleados"),
]