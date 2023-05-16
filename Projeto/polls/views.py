from django.shortcuts import render
import pyperclip as pc
from .forms import FormTutorial

from django.http import HttpResponse
from .models import Tecnologia, Tutorial, Comentario


def index(request):
    tutoriais = Tutorial.objects.all()
    palavra = ''
    tutoriais_filtrados = []

    if request.method == 'POST':
        data = request.POST
        keys = ''.join(list(data.keys()))
        if (keys.find('id') != -1):
            return tutorial(request)

        if (keys.find('palavra') != -1):
            palavra = request.POST['palavra']
            for tut in tutoriais:
                if (tut.titulo.upper().find(palavra.upper()) == 0):
                    tutoriais_filtrados.append(tut)
            context = {
                'tutoriais': tutoriais_filtrados
            }
            return render(request, 'index.html', context=context)

    context = {
        'tutoriais': tutoriais
    }

    return render(request, 'index.html', context=context)


def tutorial(request):

  tutorial = ''
  if request.method == 'POST':
    form = FormTutorial(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      id = data.get('id')
      like =  bool(data.get('like'))
      copy = bool(data.get('copy'))
      

      tutorial = Tutorial.objects.filter(id=id)
        
      if (like):
        tutorial[0].total_likes += 1
        tutorial[0].save()

      if copy:
        print('copying')
        pc.copy(tutorial[0].codigo)

    tutorial[0].total_likes += 1
    tutorial[0].save()
    print(tutorial[0].total_likes)
    print(tutorial[0].__getstate__())
    context = {
      'tutorial': tutorial,
      'id': id
    } 
    return render(request, 'tutorial.html', context=context)

    # if request.method == 'POST':
    #     data = request.POST
    #     keys = ''.join(list(data.keys()))
    #     print(keys)
    #     # print(request.POST)['like']
    #     id = 1
    #     if (keys.find('id') != -1):
    #         id = request.POST['id']

    #     tutorial = Tutorial.objects.filter(id=id)
    #     todosComentarios = Comentario.objects.all()
    #     comentarios = []
    #     for com in todosComentarios:
    #         if int(com.tutorial.id) == int(id):
    #             comentarios.append(com)

    #     if (keys.find('like') != -1):
    #         tutorial[0].total_likes += 1
    #         tutorial[0].save()

    #     if (keys.find('copy') != -1):
    #         pc.copy(tutorial[0].codigo)

    #     context = {
    #         'comentarios': comentarios,
    #         'tutorial': tutorial,
    #         'id': id
    #     }
    #     return render(request, 'tutorial.html', context=context)
