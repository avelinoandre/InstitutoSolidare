from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Apadrinhados, Padrinho
from django.contrib.auth.models import User


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
        idade = request.POST.get("idade")
        genero = request.POST.get("genero")
        foto = request.FILES.get("foto")

        if not all([nome, idade, genero, foto]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, "institutoSolidare/cadastro-apadrinhados.html")

        Apadrinhados.objects.create(
            nome=nome,
            idade=int(idade),
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

    return render(request, "institutoSolidare/informacoes-apadrinhado.html", {"apadrinhado": apadrinhado})


# views padrinhos

def cadastroPadrinhos(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")
        pais = request.POST.get("pais")
        estado = request.POST.get("estado")
        idade = request.POST.get("idade")
        data_nascimento = request.POST.get("data_nascimento")
        telefone = request.POST.get("telefone")

        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return render(request, "institutoSolidare/cadastro-padrinhos.html")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Já existe um usuário com esse e-mail.")
            return render(request, "institutoSolidare/cadastro-padrinhos.html")

        user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome)

        Padrinho.objects.create(
            user=user,
            pais=pais,
            estado=estado,
            idade=idade,
            data_nascimento=data_nascimento,
            telefone=telefone
        )

        messages.success(request, "Cadastro realizado com sucesso, agora preencha algumas informações sobre você!")
        return redirect("informacoesPadrinho")

    return render(request, "institutoSolidare/cadastro-padrinhos.html")

def informacoesPadrinho (request):
    return render(request, "institutoSolidare/informacoes-padrinho.html")
