from django.db import models


class Tecnologia(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=20)
  resumo = models.CharField(max_length=500)

  def __str__(self):
    return self.nome

class Autor(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=20)
  email = models.CharField(max_length=20)
  total_contribuicoes = models.IntegerField(default=0)

  def __str__(self):
    return self.nome

class Tutorial(models.Model):
  id = models.AutoField(primary_key=True)
  titulo = models.CharField(max_length=20)
  descricao = models.CharField(max_length=500)
  tecnologia = models.ForeignKey(Tecnologia, on_delete=models.CASCADE)
  autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
  total_likes = models.IntegerField(default=0)

  def __str__(self):
    return self.titulo


class Marcacao(models.Model):
  id = models.AutoField(primary_key=True)
  texto = models.CharField(max_length=10000)
  tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)


class Codigo(models.Model):
  id = models.AutoField(primary_key=True)
  tutoriais = models.ManyToManyField(Tutorial)
  texto = models.CharField(max_length=10000)
  autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


class Comentario(models.Model):
  id = models.AutoField(primary_key=True)
  texto = models.CharField(max_length=200)
  autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
  tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)

  def __str__(self):
    return f"Comentario de {self.autor.nome}"

