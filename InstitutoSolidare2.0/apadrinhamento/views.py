from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse

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

        if not username or not email or not password or not password_confirm:
            messages.error(request, 'Preencha todos os campos.')
        elif password != password_confirm:
            messages.error(request, 'As senhas não coincidem.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
        else:
            # Armazena os dados na sessão (sem criar o user ainda)
            request.session['novo_usuario'] = {
                'username': username,
                'email': email,
                'password': password
            }
            return redirect('padrinhoCadastro')
    return render(request, "apadrinhamento/padrinho/criar-usuario.html")

def padrinho_cadastro(request):
    novo_usuario = request.session.get('novo_usuario')

    if not novo_usuario:
        messages.error(request, 'Erro no fluxo de cadastro. Por favor, inicie novamente.')
        return redirect('padrinhoCriarUsuario')

    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        endereco = request.POST.get('endereco')
        pais = request.POST.get('pais')
        cidade = request.POST.get('cidade')
        complemento_rua = request.POST.get('complemento_rua')
        numero_rua = request.POST.get('numero_rua')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        foto_perfil = request.FILES.get('foto_perfil')

        # Cria o User agora
        user = User.objects.create_user(
            username=novo_usuario['username'],
            email=novo_usuario['email'],
            password=novo_usuario['password']
        )
        user.first_name = nome_completo
        user.save()

        # Cria o Padrinho
        Padrinho.objects.create(
            user=user,
            data_nascimento=data_nascimento,
            endereco=endereco,
            pais=pais,
            cidade=cidade,
            complemento_rua=complemento_rua,
            numero_rua=numero_rua,
            telefone=telefone,
            foto=foto_perfil,
        )

        # Login e limpeza da sessão
        login(request, user)
        request.session.pop('novo_usuario', None)

        return redirect('padrinhoEscolherApadrinhado')

    return render(request, "apadrinhamento/padrinho/cadastro.html")

@login_required
def padrinho_escolher_apadrinhado(request):
    apadrinhados = Apadrinhado.objects.all()[:3]
    return render(request, 'apadrinhamento/padrinho/escolher-apadrinhado.html', {'apadrinhados': apadrinhados})

@login_required
def padrinho_doacao(request, apadrinhado_id):
    apadrinhado = get_object_or_404(Apadrinhado, id=apadrinhado_id)

    if not hasattr(request.user, 'padrinho'):
        messages.error(request, 'Complete seu cadastro para poder doar.')
        return redirect('padrinhoCadastro')

    padrinho = request.user.padrinho

    if apadrinhado.padrinho is not None:
        messages.error(request, 'Este apadrinhado já possui um padrinho.')
        return redirect('alguma_pagina')

    apadrinhado.padrinho = padrinho
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
    padrinho = get_object_or_404(Padrinho, user=request.user)

    if request.method == 'POST':
        data = request.POST

        padrinho.user.first_name = data.get('nome', padrinho.user.first_name)
        padrinho.endereco = data.get('endereco', padrinho.endereco)
        padrinho.pais = data.get('pais', padrinho.pais)
        padrinho.cidade = data.get('cidade', padrinho.cidade)
        padrinho.complemento_rua = data.get('numero', padrinho.numero)
        padrinho.telefone = data.get('telefone', padrinho.telefone)
        padrinho.save()

        return JsonResponse({'status': 'ok', 'mensagem': 'Dados atualizados com sucesso!'})

    context = {
        'nome': padrinho.user.first_name,
        'email': request.user.email,
        'endereco': padrinho.endereco,
        'pais': padrinho.pais,
        'cidade': padrinho.cidade,
        'numero': padrinho.numero_rua,
        'complemento': padrinho.complemento_rua,
        'telefone': padrinho.telefone,
    }
    return render(request, 'apadrinhamento/padrinho/perfil.html', context)

#=====================================================================
#LOGIN ADMIN
#=====================================================================

def adm_login(request):
    return render(request, "apadrinhamento/adm-login.html")