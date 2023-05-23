from django.db import models



class Tecnologia(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    resumo = models.CharField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=200)
    total_contribuicoes = models.IntegerField(default=0)

    def __str__(self):
        return self.nome_usuario + " " + "(" + self.nome + " " + self.sobrenome + ")"


class Tutorial(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    total_likes = models.IntegerField(default=0)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo + " (by: " + self.autor.nome_usuario + ")"


class Conteudo(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=10000)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Marcacao(Conteudo):
    pass


class Codigo(Conteudo):
    linguagem = models.ForeignKey(Tecnologia, on_delete=models.CASCADE)


class TutorialConteudo(models.Model):
    id = models.AutoField(primary_key=True)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    codigo = models.ForeignKey(Codigo, null=True, blank=True, on_delete=models.CASCADE)
    marcacao = models.ForeignKey(Marcacao, null=True, blank=True, on_delete=models.CASCADE)
    ordem = models.PositiveIntegerField()

    class Meta:
        unique_together = (('tutorial', 'ordem'))
        ordering = ['ordem']


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=500)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.autor.nome_usuario + ": " + self.texto

