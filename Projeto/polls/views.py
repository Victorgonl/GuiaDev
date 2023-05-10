from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import Tecnologia


def index(request):
  tecnologias = Tecnologia.objects.all()

  context = {
    'tecnologias' : tecnologias
  }

  return render(request, 'index.html', context=context)

def guias(request):
    return render(request, 'guias.html')

def tutoriais(request):
    return render(request, 'tutoriais.html')