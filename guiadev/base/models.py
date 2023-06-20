from django.db import models
from django.db.models import Max
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.forms import ValidationError


class Tecnologia(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    resumo = models.CharField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Tecnologias"


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=200)

    def __str__(self):
        return self.username + " " + "(" + self.nome + " " + self.sobrenome + ")"

    class Meta:
        verbose_name_plural = "Usuários"


class Tutorial(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total_likes = models.IntegerField(default=0)
    tecnologias = models.ForeignKey(Tecnologia, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo + " (by: " + self.usuario.username + ")"

    class Meta:
        verbose_name_plural = "Tutoriais"


class Conteudo(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=10000)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

    class Meta:
        abstract = True
        verbose_name_plural = "Conteúdos"


class Marcacao(Conteudo):
    pass

    class Meta:
        verbose_name_plural = "Marcações"


class Codigo(Conteudo):
    linguagem = models.ForeignKey(
        Tecnologia, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Códigos"


class TutorialConteudo(models.Model):
    id = models.AutoField(primary_key=True)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    codigo = models.ForeignKey(
        Codigo, null=True, blank=True, on_delete=models.CASCADE)
    marcacao = models.ForeignKey(
        Marcacao, null=True, blank=True, on_delete=models.CASCADE)
    ordem = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        unique_together = (('tutorial', 'ordem'))
        ordering = ['tutorial', 'ordem']
        verbose_name_plural = "Conteúdos dos Tutoriais"

    def __str__(self):
        texto = ""
        if not self.codigo is None:
            texto += self.codigo.texto
        if not self.marcacao is None:
            texto += self.marcacao.texto
        return self.tutorial.titulo + " - " + str(self.ordem) + ": " + texto

    def save(self, *args, **kwargs):
        if self.codigo is None and self.marcacao is None:
            raise ValidationError(
                "É necessário fornecer um valor para 'código' ou 'marcação'.")
        if self.codigo is not None and self.marcacao is not None:
            raise ValidationError(
                "Apenas um dos campos 'código' ou 'marcaçao' pode ser preenchido.")
        if not self.ordem:
            max_ordem = TutorialConteudo.objects.filter(
                tutorial=self.tutorial).aggregate(Max('ordem'))['ordem__max']
            if max_ordem is not None:
                self.ordem = max_ordem + 1
            else:
                self.ordem = 1
        super(TutorialConteudo, self).save(*args, **kwargs)


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=500)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tutorial.titulo + " - " + self.usuario.username + ": "+ self.texto

    class Meta:
        verbose_name_plural = "Comentários"
        ordering = ['data_publicacao']


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.tutorial.titulo + " - " +  self.usuario.username

    class Meta:
        unique_together = (('usuario', 'tutorial'))
        verbose_name_plural = "Likes"
        ordering = ['tutorial', 'usuario']


@receiver(pre_delete, sender=TutorialConteudo)
def reorder_on_delete(sender, instance, **kwargs):
    remaining_objects = TutorialConteudo.objects.filter(
        tutorial=instance.tutorial).exclude(pk=instance.pk).order_by('ordem')
    instance.ordem = None
    instance.save()
    for index, obj in enumerate(remaining_objects):
        obj.ordem = index + 1
        obj.save()






