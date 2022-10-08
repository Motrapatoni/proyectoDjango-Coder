from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.DateField()
    mail = models.EmailField()