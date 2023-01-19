from django.db import models

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=30)
    sub_titulo = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id) + '-' + self.titulo + '-' + self.sub_titulo

