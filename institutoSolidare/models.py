from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Apadrinhados(models.Model):
    nome = models.CharField(max_length=200, null = False)
    idade = models.IntegerField(null = False)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=15, null = False)
    foto = models.ImageField(upload_to="fotos/")

    def __str__(self):
        return self.nome
    
class Padrinho(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    idade = models.IntegerField()
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    estilo_vida = models.IntegerField(null=True, blank=True)
    estilo_vida_outro = models.TextField(null=True, blank=True)

    area_escolar = models.IntegerField(null=True, blank=True)
    area_escolar_outro = models.TextField(null=True, blank=True)

    tempo_livre = models.IntegerField(null=True, blank=True)
    tempo_livre_outro = models.TextField(null=True, blank=True)

    inspiracao = models.IntegerField(null=True, blank=True)
    inspiracao_outro = models.TextField(null=True, blank=True)

    valor_representa = models.IntegerField(null=True, blank=True)
    valor_representa_outro = models.TextField(null=True, blank=True)

    extra = models.IntegerField(null=True, blank=True)
    extra_outro = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()