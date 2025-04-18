from django.urls import path
from institutoSolidare.views import index, admLogin, admMain, gerenciarApadrinhados, cadastrarApadrinhados

urlpatterns = [
    path("", index, name="index"),
    path("adm-login/", admLogin, name="admLogin"),
    path("adm-main/", admMain, name="admMain"),
    path("gerenciar-apadrinhados/", gerenciarApadrinhados, name="gerenciarApadrinhados"),
    path("cadastro-apadrinhados/", cadastrarApadrinhados, name="cadastroApadrinhados"),
]
