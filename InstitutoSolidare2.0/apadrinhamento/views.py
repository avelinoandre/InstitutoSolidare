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
    return render(request, "apadrinhamento/padrinho-login.html")

def cadastro_explicativo_login(request):
    return render(request, "apadrinhamento/cadastro-explicativo.html")

#=====================================================================
#LOGIN ADMIN
#=====================================================================

def adm_login(request):
    return render(request, "apadrinhamento/adm-login.html")