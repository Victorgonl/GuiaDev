from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print(request.GET.get('nome'))
    return HttpResponse("<h1>Hello</h1>" + request.GET.get('nome'))