from django.db import models

# Create your models here.
class Colaborador(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=20)
  email = models.CharField(max_length=20)
  total_contribuicoes = models.IntegerField()

  def __str__(self):
    return 'Colaborador'
    

class Tecnologia(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=20)
  descricao = models.CharField(max_length=500)

  def __str__(self):
    return 'Tecnologia'

class Guia(models.Model):
  id = models.AutoField(primary_key=True)
  titulo = models.CharField(max_length=20)
  descricao = models.CharField(max_length=500)
  tecnologia = models.ForeignKey(Tecnologia, on_delete=models.RESTRICT)
  codigo = models.CharField(max_length=500)
  colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)

  def __str__(self):
    return 'Guia'
  
class Tutorial(models.Model):
  id = models.AutoField(primary_key=True)
  titulo = models.CharField(max_length=20)
  tecnologia = models.ForeignKey(Tecnologia, on_delete=models.RESTRICT)
  descricao = models.CharField(max_length=500)
  codigo = models.CharField(max_length=500)
  colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)

  def __str__(self):
    return 'Tutorial'
  
class Ranking(models.Model):
  id = models.AutoField(primary_key=True)
  colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
  tecnologia = models.ForeignKey(Tecnologia, on_delete=models.RESTRICT)
  total_contribuicoes = models.IntegerField()

  def __str__(self):
    return 'Ranking'
