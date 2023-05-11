from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import Tecnologia



def guias(request):
    return render(request, 'guias.html')

def tutoriais(request):
    return render(request, 'tutoriais.html')



    

def index(request):
  tecnologias = Tecnologia.objects.all()
  palavra = ''

  if request.method=='POST':
    palavra = request.POST['palavra']
    tecnologias_filtradas = []
    for tec in tecnologias:
      if (tec.nome.upper().find(palavra.upper()) == 0):
        tecnologias_filtradas.append(tec)
        print(tec.nome.upper(), palavra.upper())
    
  context = {
    'tecnologias' : tecnologias_filtradas
  }

  return render(request, 'index.html', context=context)



  