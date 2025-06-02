from apadrinhamento.views import *
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    # ---------------------------------
    path("padrinho/login/", padrinho_login, name="padrinhoLogin"),
    path("padrinho/cadastro-explicativo/", padrinho_cadastro_explicativo, name="padrinhoCadastroExplicativo"),
    path("padrinho/questionario/", padrinho_questionario, name="padrinhoQuestionario"),
    path("padrinho/criar-usuario/", padrinho_criar_usuario, name="padrinhoCriarUsuario"),
    path("padrinho/cadastro/", padrinho_cadastro, name="padrinhoCadastro"),
    path("padrinho/escolher-apadrinhado/", padrinho_escolher_apadrinhado, name="padrinhoEscolherApadrinhado"),
    path("padrinho/doacao/<int:apadrinhado_id>/", padrinho_doacao, name="padrinhoDoacao"),
    path('padrinho/feed/', padrinho_feed, name='padrinhoFeed'),
    path('padrinho/perfil/', padrinho_perfil, name='padrinhoPerfil'),
    # ---------------------------------
]
