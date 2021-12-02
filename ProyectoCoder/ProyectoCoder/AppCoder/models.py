from django.db import models

# Create your models here.


class Curso(models.Model):
    #tipo de dato de la base de datos  
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Jugador(models.Model):
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.BooleanField()
