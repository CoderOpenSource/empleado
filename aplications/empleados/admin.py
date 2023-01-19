from django.contrib import admin
from .models import Empleado
from .models import Habilidades
# Register your models here.
admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'id_departamento',
        'job'
    )
    search_fields = (
        'first_name',
    )
    list_filter = (
        'job',
    )
    filter_horizontal = (
        'id_habilidad',
    )
admin.site.register(Empleado, EmpleadoAdmin)