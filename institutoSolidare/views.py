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
        foto = request.FILES.get("foto")

        if not all([nome, data_nascimento, genero, foto]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, "institutoSolidare/cadastro-apadrinhados.html")
        
        if data_nascimento:
            nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
            
            hoje = date.today()
            idade = hoje.year - nascimento.year - (
                (hoje.month, hoje.day) < (nascimento.month, nascimento.day)
        )

        Apadrinhados.objects.create(
            nome=nome,
            idade=int(idade),
            data_nascimento=data_nascimento,
            genero=genero,
            foto=foto
        )

        messages.success(request, "Apadrinhado cadastrado com sucesso!")
        return redirect("cadastroStatus")

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
            if apadrinhado.data_nascimento:
                nascimento = datetime.strptime(apadrinhado.data_nascimento, '%Y-%m-%d').date()
            
                hoje = date.today()
                idade = hoje.year - nascimento.year - (
                    (hoje.month, hoje.day) < (nascimento.month, nascimento.day)
                )
                apadrinhado.idade = idade
            # so add outros campos dps
            apadrinhado.save()
            messages.success(request, "Apadrinhado atualizado com sucesso!")
            return redirect("informacoesApadrinhados", nome=apadrinhado.nome)

    return render(request, "institutoSolidare/informacoes-apadrinhado.html", {"apadrinhado": apadrinhado})



# views padrinhos

def loginPadrinho(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        ## sem a segunda parte apos and, da pra logar como super usuario
        if (user is not None) and (not user.is_superuser):
            login(request, user)
            messages.success(request, "Login confirmado!")
            return redirect("meusAfiliados")
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, "institutoSolidare/login.html")

def meusAfiliados(request):
    return render(request, "institutoSolidare/meus-afiliados.html")

def novoAfiliado(request):
    return render(request, "institutoSolidare/novo-afiliado.html")

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

        if User.objects.filter(username=email).exists():
            messages.error(request, "Já existe um usuário com esse e-mail.")
            return render(request, "institutoSolidare/cadastro-padrinhos.html")
        
        if data_nascimento:
            nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
            
            hoje = date.today()
            idade = hoje.year - nascimento.year - (
                (hoje.month, hoje.day) < (nascimento.month, nascimento.day)
        )

        user = User.objects.create_user(username=nome, email=email, password=senha, first_name=nome)

        Padrinho.objects.create(
            user=user,
            pais=pais,
            estado=estado,
            idade=idade,
            data_nascimento=data_nascimento,
            telefone=telefone
        )

        login(request, user)

        messages.success(request, "Cadastro realizado com sucesso, agora preencha algumas informações sobre você!")
        return redirect("informacoesPadrinho")

    return render(request, "institutoSolidare/cadastro-padrinhos.html")

@login_required
def informacoesPadrinho (request):
    if request.method == "POST":
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

        padrinho = Padrinho.objects.get(user=request.user)
        padrinho.estilo_vida = resposta1
        padrinho.estilo_vida_outro = resposta1_outro if resposta1 == 99 else None

        padrinho.area_escolar = resposta2
        padrinho.area_escolar_outro = resposta2_outro if resposta2 == 99 else None

        padrinho.tempo_livre = resposta3
        padrinho.tempo_livre_outro = resposta3_outro if resposta3 == 99 else None

        padrinho.inspiracao = resposta4
        padrinho.inspiracao_outro = resposta4_outro if resposta4 == 99 else None

        padrinho.valor_representa = resposta5
        padrinho.valor_representa_outro = resposta5_outro if resposta5 == 99 else None

        padrinho.extra = resposta6
        padrinho.extra_outro = resposta6_outro if resposta6 == 99 else None

        padrinho.save()

        messages.success(request, "Informações salvas com sucesso!")
        return redirect("meusAfiliados")

    return render(request, "institutoSolidare/informacoes-padrinho.html")
