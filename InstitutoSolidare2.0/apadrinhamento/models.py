from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Apadrinhado(models.Model):
    nome = models.CharField(max_length=200, null = False)
    idade = models.IntegerField(null = False)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=15, null = False)
    foto = models.ImageField(upload_to="fotos/")
    foto_para_padrinho=models.ImageField(upload_to="fotos/")
    info = models.CharField(max_length=200, null=False)

    padrinho = models.ForeignKey('Padrinho', related_name='apadrinhados', on_delete=models.SET_NULL, null=True, blank=True)

    area_escolar = models.IntegerField(null=True, blank=True)
    profissao_desejada = models.IntegerField(null=True, blank=True)
    hobby = models.IntegerField(null=True, blank=True)
    inspiracoes = models.IntegerField(null=True, blank=True)
    valores = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Padrinho(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='padrinho')
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    numero_rua = models.CharField(max_length=50)
    complemento_rua = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30)
    foto = models.ImageField(upload_to="fotos/")

    area_escolar = models.IntegerField(null=True, blank=True)
    profissao_desejada_quando_crianca = models.IntegerField(null=True, blank=True)
    profissao_atual = models.IntegerField(null=True, blank=True)
    hobby = models.IntegerField(null=True, blank=True)
    inspiracoes = models.IntegerField(null=True, blank=True)
    valores = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()
    
class Publicacao(models.Model):
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
    
class Carta(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_envio = models.DateField(auto_now_add=True)
    aprovada = models.BooleanField(default=False)

    padrinho = models.ForeignKey(
        Padrinho,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Remetente ou destinatário, dependendo da direção da carta."
    )

    apadrinhado = models.ForeignKey(
        Apadrinhado,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Remetente ou destinatário, dependendo da direção da carta."
    )

    def __str__(self):
        return f"{self.titulo} - {'Aprovada' if self.aprovada else 'Pendente'}"