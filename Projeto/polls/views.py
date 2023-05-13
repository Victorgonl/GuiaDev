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
  tutoriais = Tutorial.objects.all()
  # palavra = ''
     

  # tutoriais_filtrados = []
  # if request.method=='POST':
  #   palavra = request.POST['palavra']
  #   for tut in tutoriais:
  #     if (tut.titulo.upper().find(palavra.upper()) == 0):
  #       tutoriais_filtrados.append(tut)
      
  if(request.method=='POST'):
    data = request.POST
    keys = ''.join(list(data.keys()))
    if(keys.find('like') != -1):
      id = request.POST['like']
      tutorial = Tutorial.objects.filter(id=id)[0]
      tutorial.total_likes += 1
      tutorial.save()

      
     



  context = {
    'tutoriais': tutoriais
  }



  

  return render(request, 'index.html', context=context)



  
  