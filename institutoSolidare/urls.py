from django.urls import path
from institutoSolidare.views import index, admLogin, admMain, gerenciarApadrinhados, cadastrarApadrinhados, cadastroStatus, cadastroPadrinhos

urlpatterns = [
    path("", index, name="index"),
    path("adm-login/", admLogin, name="admLogin"),
    path("adm-main/", admMain, name="admMain"),
    path("gerenciar-apadrinhados/", gerenciarApadrinhados, name="gerenciarApadrinhados"),
    path("cadastro-apadrinhados/", cadastrarApadrinhados, name="cadastroApadrinhados"),
    path("cadastro-status/", cadastroStatus, name="cadastroStatus"),
    path("cadastro-padrinhos/", cadastroPadrinhos, name = "cadastroPadrinhos")
]
