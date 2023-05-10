from django.contrib import admin

from django.contrib import admin

from .models import Guia
from .models import Colaborador
from .models import Ranking
from .models import Tecnologia
from .models import Tutorial

admin.site.register(Guia)
admin.site.register(Colaborador)
admin.site.register(Ranking)
admin.site.register(Tecnologia)
admin.site.register(Tutorial)

