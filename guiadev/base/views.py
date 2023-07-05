from django.shortcuts import render
from django.shortcuts import redirect, render
import pyperclip as pc
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import json
import pyperclip as pc

from .forms import AdicionarTutorialForm, TutorialForm, LoginForm, UsuarioForm
from .models import Usuario, Marcacao, Tutorial, Comentario, Codigo, TutorialConteudo, Like
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pika
import sys


def login_view(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Login inválido'})
    else:
        return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form_usuario = UsuarioForm(request.POST)
        if form.is_valid() and form_usuario.is_valid():
            form.save()
            usuario = Usuario()
            usuario.username = form.cleaned_data['username']
            usuario.nome = form_usuario.cleaned_data['nome']
            usuario.sobrenome = form_usuario.cleaned_data['sobrenome']
            usuario.save()
            return redirect('login')
    return render(request, 'register.html')


def inicio_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/index')
    return render(request, "inicio.html")


@login_required(login_url="login/")
def index_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        dadosUsuario = Usuario.objects.get(username=username)
        if request.method == 'POST':
            form = TutorialForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                print(data)
                like = bool(data.get('like'))
                id = data.get('id')
                tutoriais = Tutorial.objects.all()
                sair = bool(data.get('sair'))
                if (sair):
                    logout(request)
                    return redirect('inicio')

                if like:
                    usuario = Usuario.objects.get(username=username)
                    tutorial = Tutorial.objects.get(id=id)
                    if Like.objects.filter(usuario=usuario,
                                           tutorial=tutorial).exists():
                        like = Like.objects.get(usuario=usuario,
                                                tutorial=tutorial)
                        like.delete()
                        tutorial.__setattr__('total_likes',
                                             tutorial.total_likes - 1)
                    else:
                        like = Like(usuario=usuario, tutorial=tutorial)
                        like.save()
                        tutorial.__setattr__('total_likes',
                                             tutorial.total_likes + 1)
                    tutorial.save()
                    context = {
                        'tutoriais': tutoriais,
                        'usuario': dadosUsuario,
                    }
                    return render(request,
                                  'index.html',
                                  context=context)

                if bool(id):
                    return tutorial_view(request)

                pesquisa = data.get('pesquisa')
                tutoriais_filtrados = []
                for tut in tutoriais:
                    if (pesquisa.upper() in tut.titulo.upper()):
                        tutoriais_filtrados.append(tut)
                context = {
                    'tutoriais': tutoriais_filtrados,
                    'usuario': dadosUsuario,
                }
                return render(request, 'index.html', context=context)
        else:
            tutoriais = Tutorial.objects.all()
            context = {
                'tutoriais': tutoriais,
                'usuario': dadosUsuario,
            }
            return render(request, 'index.html', context=context)
    else:
        return HttpResponseRedirect('/index')


@login_required(login_url="login/")
def tutoriais_view(request):
    if request.method == 'GET':
        tutoriais = Tutorial.objects.all()
        usuario = request.user
        context = {'tutoriais': tutoriais, 'usuario': usuario}
        return render(request, 'tutoriais.html', context=context)
    return render(request, 'tutoriais.html')


@login_required(login_url="login/")
def tutorial_view(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #enviarEmail = bool(data.get('email_destinatario'))

            id = data.get('id')
            like = bool(data.get('like'))
            copy = bool(data.get('copy'))
            delete = bool(data.get('delete'))
            email = bool(data.get('email'))

            if (email):
                usuario = Usuario.objects.get(username=request.user.username)
                email_destinatario = usuario.email
                solicitarEnvioEmail(id, email_destinatario)
            tutorial = Tutorial.objects.get(id=id)
            tutoriais_conteudos = TutorialConteudo.objects.all()
            conteudos = []
            for tutorial_conteudo in tutoriais_conteudos:
                if tutorial_conteudo.tutorial.id == int(id):
                    if tutorial_conteudo.marcacao:
                        conteudos.append(tutorial_conteudo.marcacao)
                    elif tutorial_conteudo.codigo:
                        conteudos.append(tutorial_conteudo.codigo)
            codigos = [
                conteudo for conteudo in conteudos if type(conteudo) == Codigo
            ]
            marcacoes = [
                conteudo for conteudo in conteudos
                if type(conteudo) == Marcacao
            ]

            username = request.user.username

            if like:
                usuario = Usuario.objects.get(username=username)
                tutorial = Tutorial.objects.get(id=id)
                if Like.objects.filter(usuario=usuario,
                                       tutorial=tutorial).exists():
                    like = Like.objects.get(usuario=usuario, tutorial=tutorial)
                    like.delete()
                    tutorial.__setattr__('total_likes',
                                         tutorial.total_likes - 1)
                else:
                    like = Like(usuario=usuario, tutorial=tutorial)
                    like.save()
                    tutorial.__setattr__('total_likes',
                                         tutorial.total_likes + 1)
                tutorial.save()

            if copy:
                id_codigo = data.get('copy')
                codigo_copy = Codigo.objects.get(id=id_codigo)
                pc.copy(codigo_copy.texto)

            if delete:
                tutorial = Tutorial.objects.get(id=id)
                tutorial.delete()
                return HttpResponseRedirect('/tutoriais')

            comentario = data.get('comentario')

            if bool(comentario):
                username = request.user.username
                usuario = Usuario.objects.get(username=username)
                novo_comentario = Comentario(usuario=usuario,
                                             tutorial=tutorial,
                                             texto=comentario)
                novo_comentario.save()

            comentarios = Comentario.objects.filter(tutorial_id=id)

            context = {
                'usuario': request.user,
                'conteudos': conteudos,
                'comentarios': comentarios,
                'tutorial': tutorial,
                'id': id
            }

            return render(request, 'tutorial.html', context=context)


@login_required(login_url="login/")
def adicionar_tutorial_view(request):
    if request.method == 'POST':
        form = AdicionarTutorialForm(request.POST)
        if form.is_valid():
            data = form.data
            titulo = data.get('titulo')
            descricao = data.get('descricao')
            conteudos = data.getlist('conteudos')
            conteudos_tipo = data.getlist('conteudos_tipo')
            username = request.user.username
            usuario = Usuario.objects.get(username=username)
            tutorial = Tutorial(titulo=titulo,
                                descricao=descricao,
                                usuario=usuario)
            tutorial.save()
            for i in range(len(conteudos)):
                texto = conteudos[i]
                if conteudos_tipo[i] == "m":
                    marcacao = Marcacao(texto=texto, usuario=usuario)
                    marcacao.save()
                    tutorial_conteudo = TutorialConteudo(tutorial=tutorial,
                                                         marcacao=marcacao)
                    tutorial_conteudo.save()
                elif conteudos_tipo[i] == "c":
                    codigo = Codigo(texto=texto, usuario=usuario)
                    codigo.save()
                    tutorial_conteudo = TutorialConteudo(tutorial=tutorial,
                                                         codigo=codigo)
                    tutorial_conteudo.save()
            id = tutorial.id
            comentarios = Comentario.objects.filter(tutorial_id=id)
            tutoriais_conteudos = TutorialConteudo.objects.all()
            conteudos = []
            for tutorial_conteudo in tutoriais_conteudos:
                if tutorial_conteudo.tutorial.id == int(id):
                    if tutorial_conteudo.marcacao:
                        conteudos.append(tutorial_conteudo.marcacao)
                    elif tutorial_conteudo.codigo:
                        conteudos.append(tutorial_conteudo.codigo)

            context = {
                'usuario': request.user,
                'conteudos': conteudos,
                'comentarios': comentarios,
                'tutorial': tutorial,
                'id': id
            }
            return render(request, 'tutorial.html', context=context)
    else:
        form = AdicionarTutorialForm()
    return render(request, 'adicionar_tutorial.html', {'form': form})


def solicitarEnvioEmail(id, email):
    tutorial = Tutorial.objects.get(id=id)
    tutoriais_conteudos = TutorialConteudo.objects.all()
    conteudos = []
    for tutorial_conteudo in tutoriais_conteudos:
        if tutorial_conteudo.tutorial.id == int(id):
            if tutorial_conteudo.marcacao:
                conteudos.append(str(tutorial_conteudo.marcacao))
            elif tutorial_conteudo.codigo:
                conteudos.append("\t" + str(tutorial_conteudo.codigo))

    msg = {
        "destinatario": email,
        "autor": tutorial.usuario.username,
        "titulo": tutorial.titulo,
        "descricao": tutorial.descricao,
        "conteudos": conteudos
    }

    colocar_email_na_fila(msg)


def colocar_email_na_fila(msg):
    try:
        credentials = pika.PlainCredentials('guest', 'guest')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='172.21.0.2',port=5672, credentials=credentials)) #Docker
        # connection = pika.BlockingConnection(
            # pika.ConnectionParameters(host='localhost', credentials=credentials))  #Local
        channel = connection.channel()

        channel.queue_declare(queue='fila', durable=True)

        message = json.dumps(msg)
        channel.basic_publish(
            exchange='',
            routing_key='fila',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
        print(" [x] Sent %r" % message)
        connection.close()
    except:
        print("==============================================")
        print("Falha ao conectar com sistema de mensageria...")
        print("==============================================")
    return
