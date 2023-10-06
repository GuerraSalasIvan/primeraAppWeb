from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.


# Create Animales Models.
class Animal(models.Model):
    cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
    
    
# Create Protectora Models.
class Protectora(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
    


# Create Colaborador Models.
class Colaborador(models.Model):
    nombre = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
