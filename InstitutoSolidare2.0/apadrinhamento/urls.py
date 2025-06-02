from apadrinhamento.views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # ---------------------------------
    path("padrinho/login/", padrinho_login, name="padrinhoLogin"),
    path("padrinho/cadastro-explicativo/", padrinho_cadastro_explicativo, name="padrinhoCadastroExplicativo"),
    path("padrinho/questionario/<int:indice>/", padrinho_questionario, name="padrinhoQuestionario"),
    path('padrinho/salvar-respostas/', padrinho_salvar_respostas, name='padrinhoSalvarRespostas'),
    path("padrinho/criar-usuario/", padrinho_criar_usuario, name="padrinhoCriarUsuario"),
    path("padrinho/cadastro/", padrinho_cadastro, name="padrinhoCadastro"),
    path("padrinho/escolher-apadrinhado/", padrinho_escolher_apadrinhado, name="padrinhoEscolherApadrinhado"),
    path("padrinho/doacao/<int:apadrinhado_id>/", padrinho_doacao, name="padrinhoDoacao"),
    path('padrinho/feed/', padrinho_feed, name='padrinhoFeed'),
    path('padrinho/perfil/', padrinho_perfil, name='padrinhoPerfil'),
    path("padrinho/perfil/valores/", padrinho_alterar_valores, name="padrinhoAlterarValores"),
    path('padrinho/doacao-livre/', padrinho_doacao_livre, name='padrinhoDoacaoLivre'),
    path('padrinho/doacao-livre-checkout/', padrinho_doacao_livre_checkout, name='padrinhoDoacaoLivreCheckout'),
    path('padrinho/meus-apadrinhados/', padrinho_meus_apadrinhados, name='padrinhoMeusApadrinhados'),
    path('padrinho/cartas', padrinho_cartas, name = 'cartas'),
    path('padrinho/cartas/escrita', escrita_cartas, name = 'cartas_escrita'),
    # ---------------------------------
    path('adm/login/', adm_login ,name="admLogin"),
    path('adm/home/', adm_home, name="admHome"),
    path('adm/gerenciar-afilhados/', adm_gerenciar_afilhados, name='gerenciarAfilhados'),
    path('adm/gerenciar-feed/', adm_gerenciar_feed, name='gerenciarFeed'),
    path('adm/gerenciar-cartas/', adm_gerenciar_cartas, name='gerenciarCartas'),
]
