from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

#=====================================================================
#PÄGINA HOME
#=====================================================================

def home(request):
    return render(request, "apadrinhamento/home.html")

#=====================================================================
#LOGIN PADRINHO
#=====================================================================

def padrinho_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('padrinhoFeed')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, "apadrinhamento/padrinho/login.html")

def padrinho_cadastro_explicativo(request):
    return render(request, "apadrinhamento/padrinho/cadastro-explicativo.html")

def padrinho_questionario(request):
    return render(request, "apadrinhamento/padrinho/questionario.html")

def padrinho_criar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Verificações básicas
        if not username or not email or not password or not password_confirm:
            messages.error(request, 'Preencha todos os campos.')
        elif password != password_confirm:
            messages.error(request, 'As senhas não coincidem.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
        else:
            # Cria o usuário
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('padrinhoCadastro') 
    return render(request, "apadrinhamento/padrinho/criar-usuario.html")

@login_required
def padrinho_cadastro(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        endereco = request.POST.get('endereco')
        pais = request.POST.get('pais')
        cidade = request.POST.get('cidade')
        numero_complemento = request.POST.get('numero_complemento')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        foto_perfil = request.FILES.get('foto_perfil')

        user = request.user
        user.first_name = nome_completo  # Armazena o nome no próprio User
        user.save()

        # Cria o objeto Padrinho
        padrinho = Padrinho.objects.create(
            user=user,
            data_nascimento=data_nascimento,
            idade=0,
            pais=pais,
            estado=cidade,
            telefone=telefone,
            foto=foto_perfil,
        )

        return redirect('padrinhoEscolherApadrinhado') 
    return render(request, "apadrinhamento/padrinho/cadastro.html")

@login_required
def padrinho_escolher_apadrinhado(request):
    apadrinhados = Apadrinhados.objects.all()[:3]
    return render(request, 'apadrinhamento/padrinho/escolher-apadrinhado.html', {'apadrinhados': apadrinhados})

@login_required
def padrinho_doacao(request, apadrinhado_id):
    apadrinhado = get_object_or_404(Apadrinhados, id=apadrinhado_id)
    padrinho = request.user.padrinho  

    apadrinhado.padrinhos.add(padrinho)
    apadrinhado.save()
    return render(request, 'apadrinhamento/padrinho/doacao.html', {'apadrinhado': apadrinhado})

@login_required
def padrinho_feed(request):
    padrinho = Padrinho.objects.get(user=request.user)
    publicacoes = Publicacao.objects.filter(
        models.Q(publica=True) | models.Q(padrinho=padrinho)
    ).order_by('-data_envio')

    return render(request, 'apadrinhamento/padrinho/feed.html', {'publicacoes': publicacoes})

@login_required
def padrinho_perfil(request):
    return render(request, 'apadrinhamento/padrinho/perfil.html')

#=====================================================================
#LOGIN ADMIN
#=====================================================================

def adm_login(request):
    return render(request, "apadrinhamento/adm-login.html")