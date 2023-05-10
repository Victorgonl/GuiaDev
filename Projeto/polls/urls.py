from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("guias/", views.guias, name="guias"),
    path("tutoriais/", views.tutoriais, name="tutoriais"),
]