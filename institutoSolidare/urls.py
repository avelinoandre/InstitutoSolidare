from django.urls import path
from institutoSolidare.views import index, admLogin, admMain, gerenciarApadrinhados, cadastrarApadrinhados, \
    cadastroStatus, cadastroPadrinhos, informacoesPadrinho, informacoesApadrinhados, loginPadrinho, meusApadrinhados, novoApadrinhado, \
    infoMeuApadrinhado, escolherApadrinhado, informacoesExtrasApadrinhado

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
    path("informacoes-extras-apadrinhado/", informacoesExtrasApadrinhado, name="informacoesExtrasApadrinhado"),
    path("login/", loginPadrinho, name="login"),
    path("meus-apadrinhados", meusApadrinhados, name="meusApadrinhados"),
    path("novo-apadrinhado", novoApadrinhado, name="novoApadrinhado"),
    path("informacao-meu-apadrinhado/<str:nome>/", infoMeuApadrinhado, name = "infoMeuApadrinhado"),
    path("escolher-apadrinhado", escolherApadrinhado, name = "escolherApadrinhado")
]
