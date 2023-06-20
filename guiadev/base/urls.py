from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio_view, name="inicio"),
    path("inicio/", views.inicio_view, name="inicio"),
    path("index/", views.index_view, name="index"),
    path("tutoriais/", views.tutoriais_view, name="tutoriais"),
    path("tutorial/", views.tutorial_view, name="tutorial"),
    path("login/", views.login_view, name="login"),
    path('register/', views.register_view, name='register'),
    path("adicionar_tutorial/", views.adicionar_tutorial_view, name="adicionar_tutorial"),
]