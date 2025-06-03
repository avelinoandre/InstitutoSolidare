from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Apadrinhado(models.Model):
    nome = models.CharField(max_length=200, null = False)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=15, null = False)
    foto = models.ImageField(upload_to="fotos/")
    foto_para_padrinho=models.ImageField(upload_to="fotos/")
    info = models.CharField(max_length=200, null=False)
    endereco = models.CharField(max_length=200, null=False)

    padrinho = models.ForeignKey('Padrinho', related_name='apadrinhados', on_delete=models.SET_NULL, null=True, blank=True)

    area_escolar = models.IntegerField(null=True, blank=True)
    profissao_desejada = models.IntegerField(null=True, blank=True)
    hobby = models.IntegerField(null=True, blank=True)
    inspiracoes = models.IntegerField(null=True, blank=True)
    valores = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
    @property
    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - (
            (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )
    
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
    profissao_atual = models.IntegerField(null=True, blank=True)
    hobby = models.IntegerField(null=True, blank=True)
    inspiracoes = models.IntegerField(null=True, blank=True)
    valores = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome_completo
    
class Publicacao(models.Model):
    titulo = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="fotos/")
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
    respondida = models.BooleanField(default=False)

    padrinho = models.ForeignKey(
        "Padrinho",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Referência ao padrinho envolvido (remetente ou destinatário)."
    )

    apadrinhado = models.ForeignKey(
        "Apadrinhado",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Referência ao apadrinhado envolvido (remetente ou destinatário)."
    )

    REMETENTE_CHOICES = (
        ("padrinho", "Padrinho"),
        ("apadrinhado", "Apadrinhado"),
    )
    remetente_tipo = models.CharField(max_length=20, choices=REMETENTE_CHOICES)

    def __str__(self):
        return f"{self.titulo} - De: {self.remetente_tipo} - {'Aprovada' if self.aprovada else 'Pendente'}"

    def get_remetente(self):
        return self.padrinho if self.remetente_tipo == "padrinho" else self.apadrinhado

    def get_destinatario(self):
        return self.apadrinhado if self.remetente_tipo == "padrinho" else self.padrinho