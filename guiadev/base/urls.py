from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index_view, name="index"),
    path("tutorial/", views.tutorial_view, name="tutorial"),
    path("adicionar_tutorial/", views.adicionar_tutorial_view, name="adicionar_tutorial"),
    path("login/", views.login_view, name="login"),
    path("", views.inicio_view, name="inicio"),
    path("cadastrar/", views.cadastrar_view, name="cadastrar"),
]