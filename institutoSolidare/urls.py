from django.urls import path
from institutoSolidare.views import index, admLogin, admMain, gerenciarApadrinhados, cadastrarApadrinhados, \
    cadastroStatus, cadastroPadrinhos, informacoesPadrinho, informacoesApadrinhados, loginPadrinho, meusAfiliados, novoAfiliado

urlpatterns = [
    path("", index, name="index"),
    path("adm-login/", admLogin, name="admLogin"),
    path("adm-main/", admMain, name="admMain"),
    path("gerenciar-apadrinhados/", gerenciarApadrinhados, name="gerenciarApadrinhados"),
    path("cadastro-apadrinhados/", cadastrarApadrinhados, name="cadastroApadrinhados"),
    path("informacoes/<str:nome>/", informacoesApadrinhados, name = "informacoesApadrinhados"),
    path("cadastro-status/", cadastroStatus, name="cadastroStatus"),
    path("cadastro-padrinhos/", cadastroPadrinhos, name = "cadastroPadrinhos"),
    path("informacoes-padrinho/", informacoesPadrinho, name = "informacoesPadrinho"),
    path("login/", loginPadrinho, name="login"),
    path("meus-afiliados", meusAfiliados, name="meusAfiliados"),
    path("novo-afiliado", novoAfiliado, name="novoAfiliado"),
]
