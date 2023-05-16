from django.shortcuts import render
import pyperclip as pc
from .forms import FormTutorial

from django.http import HttpResponse
from .models import Tecnologia, Tutorial, Comentario


def index(request):
  

  if request.method == 'POST':
    form = FormTutorial(request.POST)
    if form.is_valid():
      data = form.cleaned_data

      id = data.get('id')
      if bool(id):
        return tutorial(request)
      
      pesquisa = data.get('pesquisa')
      print(pesquisa)
      tutoriais = Tutorial.objects.all()
      tutoriais_filtrados = []
      for tut in tutoriais:
        if (pesquisa.upper() in tut.titulo.upper()):
          tutoriais_filtrados.append(tut)
      
      context = {
        'tutoriais': tutoriais_filtrados
      }
      return render(request, 'index.html', context=context)
  else: 
    tutoriais = Tutorial.objects.all()
    context = {
      'tutoriais': tutoriais
    }
    return render(request, 'index.html', context=context)

def tutorial(request):

  if request.method == 'POST':
    form = FormTutorial(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      id = data.get('id')
      like =  bool(data.get('like'))
      copy = bool(data.get('copy'))

      tutorial = Tutorial.objects.get(id=id)
        
      if like:
        likes = tutorial.total_likes
        tutorial.__setattr__('total_likes', 1+likes)
        tutorial.save()

      if copy:
        pc.copy(tutorial.codigo)

      comentarios = Comentario.objects.filter(tutorial_id=id)
      context = {
        'comentarios': comentarios,
        'tutorial': [tutorial],
        'id': id
      } 
      return render(request, 'tutorial.html', context=context)

    
