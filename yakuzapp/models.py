from django.db import models

# Create your models here.

class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100) 
    link = models.URLField(null=True, blank=True)
    descripcion = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.titulo