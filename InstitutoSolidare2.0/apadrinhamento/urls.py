from apadrinhamento.views import *
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    # ---------------------------------
    path("padrinhoLogin/", padrinho_login, name="padrinhoLogin"),
    path("cadastro-explicativo/", padrinho_cadastro_explicativo, name="cadastroExplicativo"),
    path("questionario/", padrinho_questionario, name="questionario"),
    path("criar-usuario/", padrinho_criar_usuario, name="criarUsuario"),
    path("cadastro/", padrinho_cadastro, name="cadastro"),
    # ---------------------------------
]
