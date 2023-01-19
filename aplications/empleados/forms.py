from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'id_departamento',
            'avatar',
            'id_habilidad'
        )
        widgets = {
            'id_habilidad' : forms.CheckboxSelectMultiple()
        }