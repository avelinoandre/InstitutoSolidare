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
from .utils import calcular_compatibilidade
from datetime import datetime


class Pergunta:
    def __init__(self, pergunta, *respostas):
        self.pergunta = pergunta
        self.respostas = respostas
        self.resposta_usuario = 0


# =====================================================================
# PÄGINA HOME
# =====================================================================


def home(request):
    return render(request, "apadrinhamento/home.html")

def new_home(request):
    return render(request, "apadrinhamento/new_home.html")


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
        "2. E hoje, em qual área profissional você atua / Gostaria de atuar?",
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
        "3. Você possui algum hobby?",
        "Ler",
        "Cozinhar",
        "Praticar esportes",
        "Tocar instrumentos musicais",
        "Desenhar ou pintar",
        "Escrever",
        "Dançar",
    ),
    Pergunta(
        "4. O que mais te inspira hoje?",
        "Família",
        "Meus amigos",
        "Impactar positivamente a vida de outras pessoas",
        "Buscar conhecimento e crescimento",
        "Realizar sonhos de infância",
        "Fé ou espiritualidade",
    ),
    Pergunta(
        "5. E para fechar, aponte seus maior valor",
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

    perguntas_range = range(1, total_perguntas + 1)

    return render(
        request,
        "apadrinhamento/padrinho/questionario.html",
        {
            "pergunta_texto": pergunta_atual.pergunta,
            "opcoes_resposta": opcoes_resposta,
            "pergunta_atual": indice + 1,
            "total_perguntas": total_perguntas,
            "perguntas_range": perguntas_range,
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
        except Exception as e:
            messages.error(request, "Erro ao criar usuário. Tente novamente.")
            return render(request, "apadrinhamento/padrinho/cadastro.html")

        respostas = request.session.get("respostas_questionario", {})
        try:
            padrinho = Padrinho.objects.create(
                nome_completo=nome_completo,
                user=user,
                data_nascimento=datetime.strptime(data_nascimento, "%Y-%m-%d").date(),
                endereco=endereco,
                pais=pais,
                cidade=cidade,
                complemento_rua=complemento_rua,
                numero_rua=numero_rua,
                telefone=telefone,
                foto=foto_perfil if foto_perfil else None,
                area_escolar=respostas.get("resposta_0", ""),
                profissao_atual=respostas.get("resposta_1", ""),
                hobby=respostas.get("resposta_2", ""),
                inspiracoes=respostas.get("resposta_3", ""),
                valores=respostas.get("resposta_4", ""),
            )
        except Exception as e:
            messages.error(request, e)
            return render(request, "apadrinhamento/padrinho/cadastro.html")

        login(request, user)
        request.session.pop("novo_usuario", None)

        return redirect("padrinhoEscolherApadrinhadoDeslogado")

    return render(request, "apadrinhamento/padrinho/cadastro.html")

def resposta_texto(indice, pergunta_index):
    if indice is not None:
        opcoes = perguntas_padrinho[pergunta_index].respostas
        if 0 <= indice < len(opcoes):
            return opcoes[indice]
    return None

@login_required
def padrinho_escolher_apadrinhado(request):
    padrinho = request.user.padrinho
    apadrinhados_sem_padrinho = Apadrinhado.objects.filter(padrinho__isnull=True)

    apadrinhados_ordenados = sorted(
        apadrinhados_sem_padrinho,
        key=lambda ap: calcular_compatibilidade(ap, padrinho),
        reverse=True
    )

    top_3 = apadrinhados_ordenados[:3]

    for a in top_3:
        a.hobby_nome = resposta_texto(a.hobby, 2)
        a.inspiracoes_nome = resposta_texto(a.inspiracoes, 3)
        a.valores_nome = resposta_texto(a.valores, 4)
        a.area_escolar_nome = resposta_texto(a.area_escolar, 0)
        a.profissao_desejada_nome = resposta_texto(a.profissao_desejada, 1)
        a.info_texto = a.info

    return render(request, 'apadrinhamento/padrinho/escolher-apadrinhado.html', {
        'apadrinhados': top_3,
    })

@login_required
def padrinho_escolher_apadrinhado_deslogado(request):
    padrinho = request.user.padrinho
    apadrinhados_sem_padrinho = Apadrinhado.objects.filter(padrinho__isnull=True)

    apadrinhados_ordenados = sorted(
        apadrinhados_sem_padrinho,
        key=lambda ap: calcular_compatibilidade(ap, padrinho),
        reverse=True
    )

    top_3 = apadrinhados_ordenados[:3]

    for a in top_3:
        a.hobby_nome = resposta_texto(a.hobby, 2)
        a.inspiracoes_nome = resposta_texto(a.inspiracoes, 3)
        a.valores_nome = resposta_texto(a.valores, 4)
        a.area_escolar_nome = resposta_texto(a.area_escolar, 0)
        a.profissao_desejada_nome = resposta_texto(a.profissao_desejada, 1)
        a.info_texto = a.info

    return render(request, 'apadrinhamento/padrinho/escolher-apadrinhado-deslogado.html', {
        'apadrinhados': top_3,
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

    if request.method == "POST":
        publicacao_id = request.POST.get("publicacao_id")
        if publicacao_id:
            publicacao = get_object_or_404(Publicacao, id=publicacao_id)
            if not publicacao.likes.filter(id=padrinho.id).exists():
                publicacao.likes.add(padrinho)
            else:
                publicacao.likes.remove(padrinho)

        return redirect("padrinhoFeed")

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
            padrinho.profissao_atual = int(respostas_usuario[1])
            padrinho.hobby = int(respostas_usuario[2])
            padrinho.inspiracoes = int(respostas_usuario[3])
            padrinho.valores = int(respostas_usuario[4])

            padrinho.save()

            # Aqui você pode salvar no banco, etc.
            return JsonResponse({"mensagem": "Respostas salvas com sucesso!"})

        except json.JSONDecodeError:
            return JsonResponse({"mensagem": "Erro ao processar dados."}, status=400)

    padrinho = request.user.padrinho
    # GET: carregar página
    respostas_atuais = [
    padrinho.area_escolar,
    padrinho.profissao_atual,
    padrinho.hobby,
    padrinho.inspiracoes,
    padrinho.valores,
]

    # Copia as perguntas e adiciona o campo "resposta_usuario"
    perguntas = perguntas_padrinho.copy()

    for i, pergunta in enumerate(perguntas):
        pergunta.resposta_usuario = respostas_atuais[i]

    context = {
        "perguntas": perguntas,
        "respostas_usuario": [],
        "foto": padrinho.foto,
    }
    return render(request, "apadrinhamento/padrinho/alterar-valores.html", context)


@login_required
def padrinho_meus_apadrinhados(request):
    padrinho = request.user.padrinho
    apadrinhados = padrinho.apadrinhados.all()

    for a in apadrinhados:
        a.hobby_nome = resposta_texto(a.hobby, 2)
        a.inspiracoes_nome = resposta_texto(a.inspiracoes, 3)
        a.valores_nome = resposta_texto(a.valores, 4)
        a.area_escolar_nome = resposta_texto(a.area_escolar, 0)
        a.profissao_desejada_nome = resposta_texto(a.profissao_desejada, 1)
        a.info_texto = a.info

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

@login_required
def escrita_cartas(request):
    padrinho = request.user.padrinho
    apadrinhados = Apadrinhado.objects.filter(padrinho=padrinho)

    if request.method == "POST":
        afilhado_id = request.POST.get("afilhado_id")
        titulo = request.POST.get("titulo")
        conteudo = request.POST.get("conteudo")

        # Aqui você pode salvar no banco, por exemplo:
        afilhado = Apadrinhado.objects.get(id=afilhado_id)
        Carta.objects.create(
            padrinho=padrinho,
            apadrinhado=afilhado,
            titulo=titulo,
            conteudo=conteudo
        )
        return redirect("cartas_escrita")  # ou qualquer outra página de sucesso

    return render(request, "apadrinhamento/padrinho/escrita_cartas.html", {
        "apadrinhados": apadrinhados
    })


# =====================================================================
# LOGIN ADMIN
# =====================================================================

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
            if user.is_superuser:
                login(request, user)
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "error": "Acesso restrito a administradores."}, status=403)
        else:
            return JsonResponse({"success": False, "error": "Usuário ou senha inválidos."}, status=401)
    else:
        return render(request, "apadrinhamento/adm/adm-login.html")

def adm_home(request):
    return render(request, "apadrinhamento/adm/adm_home.html")

def lista_afilhados(request):
    afilhados = Apadrinhado.objects.all()
    return render(request, 'apadrinhamento/adm/gerenciar_afilhado.html', {'Apadrinhado': afilhados})

@csrf_exempt 
def editar_afilhado(request, apadrinhado_id):
    afilhado = get_object_or_404(Apadrinhado, pk=apadrinhado_id)

    if request.method == "POST":
        try:
            # Campos de texto
            nome = request.POST.get("nome")
            endereco = request.POST.get("endereco")
            info = request.POST.get("sonho")
            data_raw = request.POST.get("data_nascimento")
            data_nascimento = datetime.strptime(data_raw, "%Y-%m-%d").date() if data_raw else None

            # Arquivos
            nova_foto = request.FILES.get("foto")
            nova_foto_padrinho = request.FILES.get("foto_para_padrinho")

            # Respostas do questionário
            respostas_json = request.POST.get("respostas")
            respostas = json.loads(respostas_json) if respostas_json else []

            # Atualiza campos
            afilhado.nome = nome
            afilhado.endereco = endereco
            afilhado.info = info
            afilhado.data_nascimento = data_nascimento

            if nova_foto:
                afilhado.foto = nova_foto
            if nova_foto_padrinho:
                afilhado.foto_para_padrinho = nova_foto_padrinho

            afilhado.area_escolar = _get_or_none(respostas, 0)
            afilhado.profissao_desejada = _get_or_none(respostas, 1)
            afilhado.hobby = _get_or_none(respostas, 2)
            afilhado.inspiracoes = _get_or_none(respostas, 3)
            afilhado.valores = _get_or_none(respostas, 4)

            afilhado.save()

            return JsonResponse({
                "sucesso": True,
                "mensagem": "Afilhado atualizado com sucesso!"
            })

        except Exception as e:
            return JsonResponse({
                "sucesso": False,
                "mensagem": f"Erro ao atualizar: {str(e)}"
            }, status=400)

    # Método GET – carrega dados
    respostas_atuais = [
        afilhado.area_escolar,
        afilhado.profissao_desejada,
        afilhado.hobby,
        afilhado.inspiracoes,
        afilhado.valores,
    ]

    # Adiciona a resposta atual ao objeto de perguntas
    perguntas = perguntas_padrinho.copy()
    for i, pergunta in enumerate(perguntas):
        pergunta.resposta_usuario = respostas_atuais[i] if i < len(respostas_atuais) else None

    context = {
        "afilhado": afilhado,
        "perguntas": perguntas,
    }

    return render(request, "apadrinhamento/adm/afilhado_editar.html", context)

def excluir_afilhado(request, apadrinhado_id):
    afilhado = get_object_or_404(Apadrinhado, id=apadrinhado_id)
    afilhado.delete()
    return redirect('gerenciarAfilhados')

@csrf_exempt        # tire se já estiver usando {% csrf_token %}
def cadastrar_afilhado(request):
    if request.method == "POST":
        try:
            # Campos simples
            nome = request.POST.get("nome")
            genero = request.POST.get("genero")
            info = request.POST.get("info")
            endereco = request.POST.get("endereco")
            data_raw = request.POST.get("data_nascimento")
            data_nascimento = datetime.strptime(data_raw, "%Y-%m-%d").date() if data_raw else None

            # Respostas (vem como string JSON)
            respostas_json = request.POST.get("respostas")
            respostas = json.loads(respostas_json) if respostas_json else []

            # Arquivos
            foto = request.FILES.get("foto")
            foto_para_padrinho = request.FILES.get("foto_para_padrinho")

            # Criação
            Apadrinhado.objects.create(
                nome=nome,
                genero=genero,
                info=info,
                endereco=endereco,
                data_nascimento=data_nascimento,
                area_escolar=_get_or_none(respostas, 0),
                profissao_desejada=_get_or_none(respostas, 1),
                hobby=_get_or_none(respostas, 2),
                inspiracoes=_get_or_none(respostas, 3),
                valores=_get_or_none(respostas, 4),
                foto=foto,
                foto_para_padrinho=foto_para_padrinho,
            )

            return JsonResponse({
                "sucesso": True,
                "mensagem": "Afilhado cadastrado com sucesso!",
                "redirect_url": "/adm/gerenciar-afilhados/"
            })

        except Exception as e:
            return JsonResponse({
                "sucesso": False,
                "mensagem": f"Erro ao salvar: {str(e)}"
            }, status=400)

    return render(
        request,
        "apadrinhamento/adm/cadastrar-afilhado.html",
        {"perguntas": perguntas_padrinho},
    )

# Função auxiliar segura
def _get_or_none(lista, index):
    try:
        return lista[index]
    except (IndexError, TypeError):
        return None

# ---------- helper ----------
def _int_or_none(value):
    """Converte para int ou devolve None se vier vazio/None."""
    try:
        return int(value) if value not in (None, "") else None
    except ValueError:
        return None


def adm_gerenciar_feed(request):
    publicacoes = Publicacao.objects.all()
    return render(request, "apadrinhamento/adm/gerenciamento_feed/gerenciamento_feed_adm.html", {"publicacoes": publicacoes})

def adm_gerenciar_cartas(request):
    cartas_pendentes = Carta.objects.filter(aprovada=False, respondida=False)
    return render(request, "apadrinhamento/adm/gereciamento_cartas/caixa_entrada.html", {"cartas": cartas_pendentes})

def adm_escrever_carta(request):
    padrinhos = Padrinho.objects.all()
    cartas = Carta.objects.filter(aprovada=True)

    if request.method == "POST":
        carta_id = request.POST.get("recipient")
        titulo = request.POST.get("titulo")
        conteudo = request.POST.get("conteudo")

        carta = get_object_or_404(Carta, id=carta_id)
        padrinho = carta.padrinho

        Carta.objects.create(
            titulo=titulo,
            conteudo=conteudo,
            aprovada=True,
            padrinho=padrinho,
            apadrinhado=carta.apadrinhado,
            remetente_tipo="apadrinhado"
        )
        return redirect("gerenciarCartas")  # ou outra view apropriada

    context = {
        "padrinhos": padrinhos,
        "cartas": cartas
    }
    return render(request, "apadrinhamento/adm/gereciamento_cartas/escreva_carta.html", context)

def adm_programado(request):
    return render(request, "apadrinhamento/adm/gereciamento_cartas/programado.html")

def adm_respondidas(request):
    cartas_respondidas = Carta.objects.filter(aprovada=True, respondida=True)
    return render(request, "apadrinhamento/adm/gereciamento_cartas/cartas_respondidas.html", {"respondidas": cartas_respondidas})

@csrf_exempt
def adm_novo_post(request):
    if request.method == "POST":
        host_id   = request.POST.get("host_afiliado")  # '' se não veio nada
        titulo    = request.POST.get("titulo")
        conteudo  = request.POST.get("conteudo")
        foto      = request.FILES.get("foto")

        publica = not host_id         # True se host_id é '', None ou falsy
        apadrinhado = None
        padrinho = None
        if not publica:
            apadrinhado = get_object_or_404(Apadrinhado, id=host_id)
            padrinho = apadrinhado.padrinho

        Publicacao.objects.create(
            publica=publica,
            apadrinhado=apadrinhado,
            padrinho=padrinho,
            titulo=titulo,
            conteudo=conteudo,
            foto=foto
        )

        return JsonResponse({
            "mensagem": "Post criado com sucesso!",
            "redirect_url": reverse('gerenciarFeed')  # ou reverse('gerenciarFeed')
        })

    apadrinhados = Apadrinhado.objects.all()
    return render(request,
        "apadrinhamento/adm/gerenciamento_feed/novo_post.html",
        {"apadrinhados": apadrinhados}
    )

def adm_editar_post(request, id):
    post = get_object_or_404(Publicacao, id=id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            post.delete()
            return redirect('gerenciarFeed')  # substitua pelo nome correto

        post.titulo = request.POST.get('titulo', post.titulo)
        post.conteudo = request.POST.get('conteudo', post.conteudo)

        if 'foto' in request.FILES:
            post.foto = request.FILES['foto']

        post.save()
        return redirect('admEditarPost', id=post.id)

    return render(request, "apadrinhamento/adm/gerenciamento_feed/editar_post_adm.html", {
        "post": post
    })

def aprovar_carta(request, id):
    carta = get_object_or_404(Carta, id=id)
    carta.aprovada = True
    carta.save()
    return redirect('gerenciarCartas')

def rejeitar_carta(request, id):
    carta = get_object_or_404(Carta, id=id)
    carta.delete()
    return redirect('gerenciarCartas')
