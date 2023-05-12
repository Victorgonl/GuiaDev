from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import Tecnologia, Tutorial



def guias(request):
    return render(request, 'guias.html')

def tutoriais(request):
    return render(request, 'tutoriais.html')


def teste(request):
  if request.GET.get('mytest'):
    print('OK')
    

def index(request):
  tecnologias = Tecnologia.objects.all()
  tutoriais = Tutorial.objects.all()
  palavra = ''

  
  print(request.GET.get('mytest'))

  tutoriais_filtrados = []
  tecnologias_filtradas = []
  if request.method=='POST':
    palavra = request.POST['palavra']
    for tut in tutoriais:
      if (tut.titulo.upper().find(palavra.upper()) == 0):
        tutoriais_filtrados.append(tut)
      

  context = {
    'tutoriais': tutoriais_filtrados
  }

  return render(request, 'index.html', context=context)



  