from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "institutoSolidare/index.html")

def admLogin(request):
    return render(request, "institutoSolidare/adm-login.html")

def admMain(request):
    return render(request, "institutoSolidare/adm-main.html")

def gerenciarApadrinhados(request):
    return render(request, "institutoSolidare/gerenciar-apadrinhados.html")

def cadastrarApadrinhados(request):
    return render(request, "institutoSolidare/cadastro-apadrinhados.html")

def cadastroStatus(request):
    return render(request, "institutoSolidare/cadastro-status.html")

def cadastroPadrinhos(request):
    return render(request, "institutoSolidare/cadastro-padrinhos.html")

def informacoesPadrinho (request):
    return render(request, "institutoSolidare/informacoes-padrinho.html")