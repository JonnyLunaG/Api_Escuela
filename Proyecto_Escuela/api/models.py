from django.db import models

# Create your models here.

class Escuela(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    nombre_rector = models.CharField(max_length=30)


