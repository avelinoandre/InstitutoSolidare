from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Apadrinhados, Padrinho
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime, date

# Create your views here.

def index(request):
    return render(request, "institutoSolidare/index.html")

# views de adm

def admLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_superuser:
                login(request, user)
                return redirect("admMain")
            else:
                messages.error(request, "Apenas superusuários podem fazer login.")
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, "institutoSolidare/adm-login.html")

def admMain(request):
    return render(request, "institutoSolidare/adm-main.html")

# views de apadrinhados

def gerenciarApadrinhados(request):
    apadrinhados = Apadrinhados.objects.all()
    return render(request, "institutoSolidare/gerenciar-apadrinhados.html", {"apadrinhados" : apadrinhados})

def cadastrarApadrinhados(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        data_nascimento = request.POST.get("data_nascimento")
        genero = request.POST.get("genero")
        info = request.POST.get("info")

        if not all([nome, data_nascimento, genero]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, "institutoSolidare/cadastro-apadrinhados.html")
        
        if data_nascimento:
            nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
            
            hoje = date.today()
            idade = hoje.year - nascimento.year - (
                (hoje.month, hoje.day) < (nascimento.month, nascimento.day)
        )

        request.session["cadastro_apadrinhado_data"] = {
            "nome": nome,
            "idade": int(idade),
            "data_nascimento": data_nascimento,
            "genero": genero,
            "info": info
        }

        request.session.modified = True

        messages.success(request, "Apadrinhado cadastrado com sucesso!")
        return redirect("informacoesExtrasApadrinhado")

    return render(request, "institutoSolidare/cadastro-apadrinhados.html")

def cadastroStatus(request):
    return render(request, "institutoSolidare/cadastro-status.html")

def informacoesApadrinhados(request, nome):
    apadrinhado = get_object_or_404(Apadrinhados, nome=nome)

    if request.method == "POST":
        if "delete" in request.POST:
            apadrinhado.delete()
            messages.success(request, "Apadrinhado excluído com sucesso!")
            return redirect("gerenciarApadrinhados")

        if "save" in request.POST:
            apadrinhado.nome = request.POST.get("nome")
            apadrinhado.data_nascimento = request.POST.get("data_nascimento")
            apadrinhado.genero = request.POST.get("genero")
            apadrinhado.info = request.POST.get("info")
            if apadrinhado.data_nascimento:
                nascimento = datetime.strptime(apadrinhado.data_nascimento, '%Y-%m-%d').date()
            
                hoje = date.today()
                idade = hoje.year - nascimento.year - (
                    (hoje.month, hoje.day) < (nascimento.month, nascimento.day)
                )
                apadrinhado.idade = idade

            apadrinhado.estilo_vida = request.POST.get("estilo_vida")
            apadrinhado.area_escolar = request.POST.get("materia_preferida")
            apadrinhado.tempo_livre = request.POST.get("tempo_livre")
            apadrinhado.inspiracao = request.POST.get("inspiracao")
            apadrinhado.valor_representa = request.POST.get("representa")

            apadrinhado.palavras_chave = request.POST.get("palavras_chave")
            # so add outros campos dps
            apadrinhado.save()
            messages.success(request, "Apadrinhado atualizado com sucesso!")
            return redirect("informacoesApadrinhados", nome=apadrinhado.nome)

    return render(request, "institutoSolidare/informacoes-apadrinhado.html", {"apadrinhado": apadrinhado})



# views padrinhos

def loginPadrinho(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and not user.is_superuser and user.email == email:
            login(request, user)
            messages.success(request, "Login confirmado!")
            return redirect("meusApadrinhados")
        else:
            messages.error(request, "Usuário, email ou senha inválidos.")

    return render(request, "institutoSolidare/login.html")

def meusApadrinhados(request):
    padrinho = Padrinho.objects.get(user=request.user)
    apadrinhados = padrinho.apadrinhados.all()

    dados_apadrinhados = []
    for apadrinhado in apadrinhados:
        iniciais = ".".join([parte[0].lower() for parte in apadrinhado.nome.split()])
        data_formatada = apadrinhado.data_nascimento.strftime("%d/%m")
        dados_apadrinhados.append({
            "apadrinhado": apadrinhado,
            "iniciais": iniciais,
            "data_nascimento_formatada": data_formatada
        })

    context = {
        "dados_apadrinhados": dados_apadrinhados
    }

    return render(request, "institutoSolidare/meus-apadrinhados.html", context)

def infoMeuApadrinhado(request, nome):
    apadrinhado = get_object_or_404(Apadrinhados, nome=nome)

    iniciais = ".".join([parte[0].lower() for parte in apadrinhado.nome.split()])

    dataNascimentoFormatada = apadrinhado.data_nascimento.strftime("%d/%m")

    context = {
        "apadrinhado": apadrinhado,
        "iniciais": iniciais,
        "dataNascimentoFormatada": dataNascimentoFormatada
    }

    return render(request, "institutoSolidare/informacoes-meu-apadrinhado.html", context)

def novoApadrinhado(request):
    return render(request, "institutoSolidare/novo-apadrinhado.html")

@login_required
def escolherApadrinhado(request):
    if request.method == "POST":
        padrinho = get_object_or_404(Padrinho, user=request.user)
        selecionados_ids = request.POST.getlist("apadrinhados")

        for apadrinhado_id in selecionados_ids:
            apadrinhado = get_object_or_404(Apadrinhados, id=apadrinhado_id)
            apadrinhado.padrinhos.add(padrinho)

        messages.success(request, "Apadrinhados selecionados com sucesso!")
        return redirect("meusApadrinhados")

    apadrinhados_disponiveis = Apadrinhados.objects.exclude(padrinhos=request.user.padrinho)

    apadrinhados_formatados = []
    for apadrinhado in apadrinhados_disponiveis:
        iniciais = ".".join([parte[0] for parte in apadrinhado.nome.split()])
        data_nasc = apadrinhado.data_nascimento.strftime("%d/%m")
        apadrinhados_formatados.append({
            "id": apadrinhado.id,
            "iniciais": iniciais,
            "idade": apadrinhado.idade,
            "data_nascimento": data_nasc,
            "foto": apadrinhado.foto
        })

    context = {
        "apadrinhados": apadrinhados_formatados
    }
    return render(request, "institutoSolidare/escolher-apadrinhados.html", context)


def cadastroPadrinhos(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")
        pais = request.POST.get("pais")
        estado = request.POST.get("estado")
        data_nascimento = request.POST.get("data_nascimento")
        telefone = request.POST.get("telefone")

        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return render(request, "institutoSolidare/cadastro-padrinhos.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Já existe um usuário com esse e-mail.")
            return render(request, "institutoSolidare/cadastro-padrinhos.html")

        request.session["cadastro_user_data"] = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "pais": pais,
            "estado": estado,
            "data_nascimento": data_nascimento,
            "telefone": telefone
        }

        request.session.modified = True

        messages.success(request, "Cadastro básico feito! Agora complete suas informações.")
        return redirect("informacoesPadrinho")

    return render(request, "institutoSolidare/cadastro-padrinhos.html")

def informacoesPadrinho (request):
    if request.method == "POST":
        cadastro_data = request.session.get("cadastro_user_data")

        if not cadastro_data:
            messages.error(request, "Erro ao recuperar os dados do cadastro.")
            return redirect("cadastroPadrinhos")
        
        user = User.objects.create_user(
            username=cadastro_data["email"],  # ou pode usar o nome
            email=cadastro_data["email"],
            password=cadastro_data["senha"],
            first_name=cadastro_data["nome"]
        )

        login(request, user)

        nascimento = datetime.strptime(cadastro_data["data_nascimento"], "%Y-%m-%d").date()
        hoje = date.today()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

        resposta1 = int(request.POST.get("estilo_vida"))
        resposta1_outro = request.POST.get("estilo_vida_outro", "").strip()

        resposta2 = int(request.POST.get("materia_preferida"))
        resposta2_outro = request.POST.get("materia_preferida_outro", "").strip()

        resposta3 = int(request.POST.get("tempo_livre"))
        resposta3_outro = request.POST.get("tempo_livre_outro", "").strip()

        resposta4 = int(request.POST.get("inspiracao"))
        resposta4_outro = request.POST.get("inspiracao_outro", "").strip()

        resposta5 = int(request.POST.get("representa"))
        resposta5_outro = request.POST.get("representa_outro", "").strip()

        resposta6 = int(request.POST.get("extra"))
        resposta6_outro = request.POST.get("extra_outro", "").strip()

        # Cria o padrinho
        Padrinho.objects.create(
            user=user,
            pais=cadastro_data["pais"],
            estado=cadastro_data["estado"],
            data_nascimento=nascimento,
            idade=idade,
            telefone=cadastro_data["telefone"],
            estilo_vida=resposta1,
            estilo_vida_outro=resposta1_outro if resposta1 == 99 else None,
            area_escolar = resposta2,
            area_escolar_outro = resposta2_outro if resposta2 == 99 else None,
            tempo_livre = resposta3,
            tempo_livre_outro = resposta3_outro if resposta3 == 99 else None,
            inspiracao = resposta4,
            inspiracao_outro = resposta4_outro if resposta4 == 99 else None,
            valor_representa = resposta5,
            valor_representa_outro = resposta5_outro if resposta5 == 99 else None,
            extra = resposta6,
            extra_outro = resposta6_outro if resposta6 == 99 else None
        )

        request.session.pop("cadastro_user_data", None)

        messages.success(request, "Informações salvas com sucesso!")
        return redirect("escolherApadrinhado")

    return render(request, "institutoSolidare/informacoes-padrinho.html")

def informacoesExtrasApadrinhado (request):
    if request.method == "POST":
        apadrinhado_data = request.session.get("cadastro_apadrinhado_data")
        foto = request.FILES.get("foto")
        foto_para_padrinho = request.FILES.get("foto_para_padrinho")
        Apadrinhados.objects.create(
            nome=apadrinhado_data["nome"],
            idade=apadrinhado_data["idade"],
            data_nascimento=apadrinhado_data["data_nascimento"],
            genero=apadrinhado_data["genero"],
            info=apadrinhado_data["info"],
            foto=foto,
            foto_para_padrinho=foto_para_padrinho,
            estilo_vida = int(request.POST.get("estilo_vida")),
            area_escolar = int(request.POST.get("materia_preferida")),
            tempo_livre = int(request.POST.get("tempo_livre")),
            inspiracao = int(request.POST.get("inspiracao")),
            valor_representa = int(request.POST.get("representa")),
            palavras_chave = request.POST.get("palavras_chave"),
        )
        request.session.pop("cadastro_apadrinhado_data", None)

        messages.success(request, "Informações salvas com sucesso!")
        return redirect("admMain")
    return render(request, "institutoSolidare/informacoes-extras-apadrinhado.html")