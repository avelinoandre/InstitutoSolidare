from django.db import models

# Create your models here.

class Apadrinhados(models.Model):
    nome = models.CharField(max_length=200, null = False)
    idade = models.IntegerField(null = False)
    genero = models.CharField(max_length=15, null = False)
    foto = models.ImageField(upload_to="fotos/")