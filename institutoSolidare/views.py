from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Apadrinhados


# Create your views here.

def index(request):
    return render(request, "institutoSolidare/index.html")

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

def cadastroPadrinhos(request):
    return render(request, "institutoSolidare/cadastro-padrinhos.html")

def informacoesPadrinho (request):
    return render(request, "institutoSolidare/informacoes-padrinho.html")