from apadrinhamento.views import *
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("login/", padrinho_login, name="padrinhoLogin"),
    path("cadastro-explicativo/", cadastro_explicativo_login, name="cadastroExplicativo"),
]
