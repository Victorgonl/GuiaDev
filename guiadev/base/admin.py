from django.contrib import admin
from .models import Comentario, Tecnologia, Tutorial, Codigo, Marcacao, TutorialConteudo, Usuario, Like

admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Tecnologia)
admin.site.register(Tutorial)
admin.site.register(Codigo)
admin.site.register(Marcacao)
admin.site.register(TutorialConteudo)
admin.site.register(Like)