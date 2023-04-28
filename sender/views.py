from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.GET.get('mytest'):
        print('OK')
    return render(request,'index.html')