from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Apadrinhados(models.Model):
    nome = models.CharField(max_length=200, null = False)
    idade = models.IntegerField(null = False)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=15, null = False)
    foto = models.ImageField(upload_to="fotos/")
    foto_para_padrinho=models.ImageField(upload_to="fotos/")
    info = models.CharField(max_length=200, null=False)

    padrinhos = models.ManyToManyField('Padrinho', related_name='apadrinhados', blank=True)

    area_escolar = models.IntegerField(null=True, blank=True)
    profissao_desejada = models.IntegerField(null=True, blank=True)
    hobby = models.IntegerField(null=True, blank=True)
    inspiracoes = models.IntegerField(null=True, blank=True)
    valores = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Padrinho(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    idade = models.IntegerField()
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="fotos/")

    area_escolar = models.IntegerField(null=True, blank=True)
    profissao_desejada_quando_crianca = models.IntegerField(null=True, blank=True)
    profissao_atual = models.IntegerField(null=True, blank=True)
    hobby = models.IntegerField(null=True, blank=True)
    inspiracoes = models.IntegerField(null=True, blank=True)
    valores = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()
    
class Carta(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_envio = models.DateField(auto_now_add=True)
    
    publica = models.BooleanField(default=False)  # True = pública, False = privada
    padrinho = models.ForeignKey(
        Padrinho,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Somente para cartas privadas. Deixe em branco para cartas públicas."
    )

    def __str__(self):
        if self.publica:
            return f"Carta pública: {self.titulo}"
        return f"Carta privada para {self.padrinho.user.get_full_name()}"