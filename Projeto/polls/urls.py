from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("guias/", views.guias, name="guias"),
    path("tutorial/", views.tutorial, name="tutorial"),
]