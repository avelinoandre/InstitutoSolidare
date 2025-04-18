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