from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tutorial/", views.tutorial, name="tutorial"),
    path("adicionar_tutorial/", views.adicionar_tutorial, name="adicionar_tutorial"),
    path("test/", views.test, name="tutorial"),
]