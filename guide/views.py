from django.shortcuts import render
from guide.models import Guia

# Create your views here.


from django.http import HttpResponse


def index(request):
  # guia = Guia(guia_titulo='Guia  python', guia_tecnologia='Python', guia_descricao='Python básico', guia_codigo='***nome = "Joao" \n print(nome)***')
  # guia.save()
  guias = Guia.objects.all()
   
  context = {
    'guias': guias,
  }
  return render(request, 'index.html', context=context)

def guias(request):
    return render(request, 'guias.html')

def tutoriais(request):
    return render(request, 'tutoriais.html')