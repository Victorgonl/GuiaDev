from django.contrib import admin
from .models import Autor,Comentario,Tecnologia,Tutorial, Codigo, Marcacao, TutorialConteudo, Usuario

admin.site.register(Autor)
admin.site.register(Comentario)
admin.site.register(Tecnologia)
admin.site.register(Tutorial)
admin.site.register(Codigo)
admin.site.register(Marcacao)
admin.site.register(TutorialConteudo)
admin.site.register(Usuario)


