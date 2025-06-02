from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ObjectDoesNotExist


class Pergunta:
    def __init__(self, pergunta, *respostas):
        self.pergunta = pergunta
        self.respostas = respostas


# =====================================================================
# PÄGINA HOME
# =====================================================================


def home(request):
    return render(request, "apadrinhamento/home.html")


# =====================================================================
# LOGIN PADRINHO
# =====================================================================


def padrinho_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("padrinhoFeed")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, "apadrinhamento/padrinho/login.html")


def padrinho_cadastro_explicativo(request):
    return render(request, "apadrinhamento/padrinho/cadastro-explicativo.html")


perguntas_padrinho = [
    Pergunta(
        "1. Na escola, qual área te chamava mais atenção?",
        "Linguagens",
        "Matemática",
        "Ciências da Natureza",
        "Ciências Humanas",
        "Artes",
    ),
    Pergunta(
        "2. Qual era a profissão dos seus sonhos, quando criança?",
        "Médico(a)",
        "Professor(a)",
        "Bombeiro(a)",
        "Atleta ou Jogador(a) de futebol",
        "Artista",
        "Ator",
        "Engenheiro(a)",
        "Arquiteto(a)",
        "Veterinário(a)",
        "Empresário(a)",
        "Juiz",
    ),
    Pergunta(
        "3. E hoje, em qual área profissional você atua?",
        "Saúde",
        "Educação",
        "Legislativa",
        "Tecnologia",
        "Negócios",
        "Engenharia",
        "Artes e Cultura",
        "Comunicação e Marketing",
        "Esportes/Atividades físicas",
        "Serviço público",
    ),
    Pergunta(
        "4. Você possui algum hobby?",
        "Ler",
        "Cozinhar",
        "Praticar esportes",
        "Tocar instrumentos musicais",
        "Desenhar ou pintar",
        "Escrever",
        "Dançar",
    ),
    Pergunta(
        "5. O que mais te inspira hoje?",
        "Família",
        "Meus amigos",
        "Impactar positivamente a vida de outras pessoas",
        "Buscar conhecimento e crescimento",
        "Realizar sonhos de infância",
        "Fé ou espiritualidade",
    ),
    Pergunta(
        "6. E para fechar, aponte seus 3 maiores valores",
        "Honestidade",
        "Liberdade",
        "Respeito",
        "Amor",
        "Coragem",
        "Justiça",
        "Empatia",
        "Responsabilidade",
        "Gratidão",
        "Fé",
        "Determinação",
        "Lealdade",
    ),
]


def padrinho_questionario(request, indice=0):
    pergunta_atual = perguntas_padrinho[indice]
    opcoes_resposta = list(enumerate(pergunta_atual.respostas))
    total_perguntas = len(perguntas_padrinho)

    return render(
        request,
        "apadrinhamento/padrinho/questionario.html",
        {
            "pergunta_texto": pergunta_atual.pergunta,
            "opcoes_resposta": opcoes_resposta,
            "pergunta_atual": indice,
            "total_perguntas": total_perguntas,
            "pergunta_anterior_url": (
                reverse("padrinhoQuestionario", args=[indice - 1])
                if indice > 0
                else "#"
            ),
        },
    )


@csrf_exempt
def padrinho_salvar_respostas(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        request.session["respostas_questionario"] = dados
        return JsonResponse({"status": "ok"})
    return JsonResponse({"error": "Método inválido"}, status=400)


def padrinho_criar_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if not username or not email or not password or not password_confirm:
            messages.error(request, "Preencha todos os campos.")
        elif password != password_confirm:
            messages.error(request, "As senhas não coincidem.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Este nome de usuário já está em uso.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está cadastrado.")
        else:
            # Armazena os dados na sessão (sem criar o user ainda)
            request.session["novo_usuario"] = {
                "username": username,
                "email": email,
                "password": password,
            }
            return redirect("padrinhoCadastro")
    return render(request, "apadrinhamento/padrinho/criar-usuario.html")


def padrinho_cadastro(request):
    novo_usuario = request.session.get("novo_usuario")

    if not novo_usuario:
        messages.error(request, "Erro no fluxo de cadastro. Por favor, inicie novamente.")
        return redirect("padrinhoCriarUsuario")

    if request.method == "POST":
        nome_completo = request.POST.get("nome_completo", "").strip()
        endereco = request.POST.get("endereco", "").strip()
        pais = request.POST.get("pais", "").strip()
        cidade = request.POST.get("cidade", "").strip()
        complemento_rua = request.POST.get("complemento_rua", "").strip()
        numero_rua = request.POST.get("numero_rua", "").strip()
        telefone = request.POST.get("telefone", "").strip()
        data_nascimento = request.POST.get("data_nascimento", "").strip()
        foto_perfil = request.FILES.get("foto_perfil")

        campos_obrigatorios = [
            ("Nome completo", nome_completo),
            ("Endereço", endereco),
            ("País", pais),
            ("Cidade", cidade),
            ("Número da rua", numero_rua),
            ("Telefone", telefone),
            ("Data de nascimento", data_nascimento),
        ]

        erros = []

        for nome, valor in campos_obrigatorios:
            if not valor:
                erros.append(f"Campo obrigatório: {nome}")

        if erros:
            for erro in erros:
                messages.error(request, erro)
            return render(request, "apadrinhamento/padrinho/cadastro.html")

        try:
            user = User.objects.create_user(
                username=novo_usuario["username"],
                email=novo_usuario["email"],
                password=novo_usuario["password"],
            )
            user.save()
        except Exception as e:
            messages.error(request, "Erro ao criar usuário. Tente novamente.")
            return render(request, "apadrinhamento/padrinho/cadastro.html")

        respostas = request.session.get("respostas_questionario", {})

        try:
            padrinho = Padrinho.objects.create(
                nome_completo=nome_completo,
                user=user,
                data_nascimento=data_nascimento,
                endereco=endereco,
                pais=pais,
                cidade=cidade,
                complemento_rua=complemento_rua,
                numero_rua=numero_rua,
                telefone=telefone,
                foto=foto_perfil if foto_perfil else None,
                area_escolar=respostas.get("resposta_0", ""),
                profissao_desejada_quando_crianca=respostas.get("resposta_1", ""),
                profissao_atual=respostas.get("resposta_2", ""),
                hobby=respostas.get("resposta_3", ""),
                inspiracoes=respostas.get("resposta_4", ""),
                valores=respostas.get("resposta_5", ""),
            )
        except Exception as e:
            messages.error(request, "Erro ao salvar os dados. Tente novamente.")
            return render(request, "apadrinhamento/padrinho/cadastro.html")

        login(request, user)
        request.session.pop("novo_usuario", None)

        return redirect("padrinhoEscolherApadrinhado")

    return render(request, "apadrinhamento/padrinho/cadastro.html")


@login_required
def padrinho_escolher_apadrinhado(request):
    apadrinhados_sem_padrinho = Apadrinhado.objects.filter(padrinho__isnull=True)
    
    return render(request, 'apadrinhamento/padrinho/escolher-apadrinhado.html', {
        'apadrinhados': apadrinhados_sem_padrinho
    })


@login_required
@csrf_exempt
def padrinho_doacao(request, apadrinhado_id):
    apadrinhado = get_object_or_404(Apadrinhado, id=apadrinhado_id)

    # Evita reprocessar se já estiver afiliado
    if apadrinhado.padrinho is not None:
        return redirect('padrinhoFeed')  # ou uma página de erro personalizada

    if request.method == "POST":
        padrinho = request.user.padrinho
        apadrinhado.padrinho = padrinho
        apadrinhado.save()
        return JsonResponse({"status": "ok"})

    return render(
        request, "apadrinhamento/padrinho/doacao.html", {"apadrinhado": apadrinhado}
    )


@login_required
def padrinho_feed(request):
    padrinho = Padrinho.objects.get(user=request.user)
    publicacoes = Publicacao.objects.filter(
        models.Q(publica=True) | models.Q(padrinho=padrinho)
    ).order_by("-data_envio")

    return render(
        request, "apadrinhamento/padrinho/feed.html", {"publicacoes": publicacoes}
    )


@login_required
def padrinho_perfil(request):
    try:
        padrinho = request.user.padrinho
    except ObjectDoesNotExist:
        return JsonResponse(
            {"status": "error", "mensagem": "Perfil de padrinho não encontrado."}
        )

    if request.method == "POST":
        # Dados do modelo Padrinho
        padrinho.nome_completo = request.POST.get("nome", "").strip()
        padrinho.endereco = request.POST.get("endereco", "").strip()
        padrinho.pais = request.POST.get("pais", "").strip()
        padrinho.cidade = request.POST.get("cidade", "").strip()
        padrinho.numero_rua = request.POST.get("numero", "").strip()
        padrinho.complemento_rua = request.POST.get("complemento", "").strip()
        padrinho.telefone = request.POST.get("telefone", "").strip()

        # Atualiza a imagem, se enviada
        if "foto" in request.FILES:
            padrinho.foto = request.FILES["foto"]

        try:
            padrinho.user.save()
            padrinho.save()
            return JsonResponse(
                {
                    "status": "ok",
                    "mensagem": "Dados atualizados com sucesso!",
                    "nova_foto_url": padrinho.foto.url if padrinho.foto else "",
                }
            )
        except Exception as e:
            return JsonResponse({"status": "error", "mensagem": str(e)})

    # GET - renderiza o template com os dados do padrinho
    context = {
        "nome": padrinho.nome_completo,
        "email": padrinho.user.email,
        "endereco": padrinho.endereco,
        "pais": padrinho.pais,
        "cidade": padrinho.cidade,
        "numero": padrinho.numero_rua,
        "complemento": padrinho.complemento_rua,
        "telefone": padrinho.telefone,
        "foto": padrinho.foto,
    }
    return render(request, "apadrinhamento/padrinho/perfil.html", context)


def padrinho_doacao_livre(request):
    return render(request, "apadrinhamento/padrinho/doacao-livre.html")


def padrinho_doacao_livre_checkout(request):
    return render(request, "apadrinhamento/padrinho/doacao-livre-checkout.html")


@login_required
def padrinho_alterar_valores(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            respostas_usuario = data.get("respostas", [])
            padrinho = request.user.padrinho

            padrinho.area_escolar = int(respostas_usuario[0])
            padrinho.profissao_desejada_quando_crianca = int(respostas_usuario[1])
            padrinho.profissao_atual = int(respostas_usuario[2])
            padrinho.hobby = int(respostas_usuario[3])
            padrinho.inspiracoes = int(respostas_usuario[4])
            padrinho.valores = int(respostas_usuario[5])

            padrinho.save()

            # Aqui você pode salvar no banco, etc.
            return JsonResponse({"mensagem": "Respostas salvas com sucesso!"})

        except json.JSONDecodeError:
            return JsonResponse({"mensagem": "Erro ao processar dados."}, status=400)

    # GET: carregar página
    context = {
        "perguntas": perguntas_padrinho,
        "respostas_usuario": [],
    }
    return render(request, "apadrinhamento/padrinho/alterar-valores.html", context)


@login_required
def padrinho_meus_apadrinhados(request):
    padrinho = request.user.padrinho
    apadrinhados = padrinho.apadrinhados.all()
    return render(
        request,
        "apadrinhamento/padrinho/meus-apadrinhados.html",
        {"apadrinhados": apadrinhados},
    )


@login_required
def padrinho_cartas(request):
    padrinho = request.user.padrinho

    cartas_recebidas = Carta.objects.filter(
        padrinho=padrinho, remetente_tipo="apadrinhado", aprovada=True
    ).order_by("-data_envio")

    context = {"cartas_recebidas": cartas_recebidas}
    return render(request, "apadrinhamento/padrinho/cartas.html", context)


# =====================================================================
# LOGIN ADMIN
# =====================================================================

perguntas_apadrinhado = [
    Pergunta(
        "1. Qual matéria  da escola você mais gosta?",
        "Português (Linguagens)",
        "Inglês (Linguagens)",
        "Matemática",
        "Ciências",
        "Historia (Humanas)",
        "Geografia (Humanas)",
        "Artes",
    ),
    Pergunta(
        "2. Você quer ser o que quando crescer?",
        "Médico(a)",
        "Professor(a)",
        "Bombeiro(a)",
        "Atleta ou Jogador(a) de futebol",
        "Artista",
        "Ator",
        "Engenheiro(a)",
        "Arquiteto(a)",
        "Veterinário(a)",
        "Empresário(a)",
        "Juiz",
    ),
    Pergunta(
        "3. Você possui algum hobby?",
        "Saúde",
        "Educação",
        "Legislativa",
        "Tecnologia",
        "Negócios",
        "Engenharia",
        "Artes e Cultura",
        "Comunicação e Marketing",
        "Esportes/Atividades físicas",
        "Serviço público",
    ),
    Pergunta(
        "4. O que mais te inspira hoje? (O que faz o seu olho brilhar e querer estudar?)",
        "Ler",
        "Cozinhar",
        "Praticar esportes",
        "Tocar instrumentos musicais",
        "Desenhar ou pintar",
        "Escrever",
        "Dançar",
    ),
    Pergunta(
        "5. Escolha 3 valores que você acha importante e quer levar para a vida",
        "Família",
        "Meus amigos",
        "Impactar positivamente a vida de outras pessoas",
        "Buscar conhecimento e crescimento",
        "Realizar sonhos de infância",
        "Fé ou espiritualidade",
    ),
]

def adm_login(request):
    if request.method == "POST" and request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
        except Exception:
            return JsonResponse({"success": False, "error": "Dados inválidos"}, status=400)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "Usuário ou senha inválidos."})
    else:
        # Se acessar via GET, mostra a página
        return render(request, "apadrinhamento/adm/adm-login.html")

def adm_home(request):
    return render(request, "apadrinhamento/adm/adm_home.html")


def gerenciar_afilhados(request):
    return render(request, "apadrinhamento/adm/gerenciar_afilhados.html")


def gerenciar_feed(request):
    return render(request, "apadrinhamento/adm/gerenciar_feed.html")


def gerenciar_cartas(request):
    return render(request, "apadrinhamento/adm/gerenciar_cartas.html")
