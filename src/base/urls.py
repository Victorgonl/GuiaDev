from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("tutorial/", views.tutorial, name="tutorial"),
    path("adicionar_tutorial/", views.adicionar_tutorial, name="adicionar_tutorial"),
    path("login/", views.loginView, name="login"),
    path("", views.inicio, name="inicio"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
]