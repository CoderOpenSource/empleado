from django.db import models
from aplications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO')
                   )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombre Completo', max_length=80, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank= True, null=True)
    id_habilidad = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()


    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name