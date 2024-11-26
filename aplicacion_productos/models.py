from django.db import models

# Create your models here.
class Productos(models.Model):
    codigoProducto = models.IntegerField()
    descripcionProducto = models.CharField(max_length=255)
    estatus = models.BooleanField()