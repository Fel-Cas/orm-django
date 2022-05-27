from django.db import models

#managers
from .managers import AutorManager

# Create your models here.

class Autor(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos= models.CharField( max_length=50)
    nacionalidad=models.CharField( max_length=50)
    edad=models.PositiveIntegerField()    

    ## Conectamos el manager con el modelo
    objects=AutorManager()
    def __str__(self):
        return f'{self.nombres}  {self.apellidos} '