from django.shortcuts import render

#=====================================================================
#PÄGINA HOME
#=====================================================================

def home(request):
    return render(request, "apadrinhamento/home.html")

#=====================================================================
#LOGIN PADRINHO
#=====================================================================

def padrinho_login(request):
    return render(request, "apadrinhamento/padrinho/padrinho-login.html")

def padrinho_cadastro_explicativo(request):
    return render(request, "apadrinhamento/padrinho/cadastro-explicativo.html")

def padrinho_questionario(request):
    return render(request, "apadrinhamento/padrinho/questionario.html")

def padrinho_criar_usuario(request):
    return render(request, "apadrinhamento/padrinho/criar-usuario.html")

def padrinho_cadastro(request):
    return render(request, "apadrinhamento/padrinho/cadastro.html")

#=====================================================================
#LOGIN ADMIN
#=====================================================================

def adm_login(request):
    return render(request, "apadrinhamento/adm-login.html")