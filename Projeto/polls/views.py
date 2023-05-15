from django.shortcuts import render
import pyperclip as pc
# Create your views here.


from django.http import HttpResponse
from .models import Tecnologia, Tutorial, Comentario


def index(request):
  print('index')
  tutoriais = Tutorial.objects.all()
  palavra = ''
  tutoriais_filtrados = []

  if request.method=='POST':
    data = request.POST
    keys = ''.join(list(data.keys()))
    if(keys.find('id-tutorial') != -1):
      return tutorial(request)
      

    if(keys.find('palavra') != -1):
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
  if request.method=='POST':
    data = request.POST
    keys = ''.join(list(data.keys()))
    print(keys)
    if(keys.find('id-tutorial') != -1):     
      id = request.POST['id-tutorial']
      tutorial = Tutorial.objects.filter(id=id)

      todosComentarios = Comentario.objects.all()
      comentarios = []
      for com in todosComentarios:
        if int(com.tutorial.id) == int(id):
          comentarios.append(com)
      print(comentarios)

      context = {
        'comentarios': comentarios,
        'tutorial': tutorial
      }
      return render(request, 'tutorial.html', context=context)
    if(keys.find('like') != -1):
      id = request.POST['like']
      tutorial = Tutorial.objects.filter(id=id)[0]
      tutorial.total_likes += 1
      tutorial.save()
      context = {
        'tutorial': [tutorial]
      }
      return render(request, 'tutorial.html', context=context)
    
    if(keys.find('copy') != -1):
      id = request.POST['copy']
      tutorial = Tutorial.objects.filter(id=id)[0]
      pc.copy(tutorial.codigo)
      context = {
        'tutorial': [tutorial]
      }
      return render(request, 'tutorial.html', context=context)


  # tutoriais = Tutorial.objects.all()

  # if(request.method=='POST'):
  #   data = request.POST
  #   keys = ''.join(list(data.keys()))
  #   if(keys.find('like') != -1):
  #     id = request.POST['like']
  #     tutorial = Tutorial.objects.filter(id=id)[0]
  #     tutorial.total_likes += 1
  #     tutorial.save()

  #   if(keys.find('copy') != -1):
  #     code = request.POST['copy']
  #     pc.copy(code)
  #     print(code)      
    
  # return render(request, 'tutorial.html')





def guias(request):
    return render(request, 'guias.html')




    

  



  
  