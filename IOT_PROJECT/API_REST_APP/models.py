from django.db import models

# Create your models here.

class sensores(models.Model):
    Tag=models.CharField(max_length=8)
    Ubicacion=models.CharField(max_length=50)    
    Medicion=models.CharField(max_length=50)
    Valor=models.IntegerField()
    Fecha=models.DateField()

