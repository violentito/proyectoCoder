from django.db import models

# Create your models here.


class Curso(models.Model):
    #tipo de dato de la base de datos  
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f'CURSO: {self.nombre} CAMADA: {self.camada}'
 
class Estudiante(models.Model):
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    espromedio = models.IntegerField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apllido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)

class Entregable(models.Model):
    numeroDeClase = models.IntegerField()
    estado = models.BooleanField()
    nota = models.IntegerField

class Jugador(models.Model):
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.IntegerField()