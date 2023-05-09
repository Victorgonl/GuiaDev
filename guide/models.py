from django.db import models

# Create your models here.

class Guia(models.Model):
  guia_id = models.AutoField(primary_key=True)
  guia_titulo = models.CharField(max_length=20)
  guia_tecnologia = models.CharField(max_length=20)
  guia_descricao = models.CharField(max_length=500)
  guia_codigo = models.CharField(max_length=500)