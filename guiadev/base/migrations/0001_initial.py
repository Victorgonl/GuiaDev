# Generated by Django 4.2.1 on 2023-06-06 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('resumo', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tecnologias',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=1000)),
                ('total_likes', models.IntegerField(default=0)),
                ('tecnologias', models.ManyToManyField(to='base.tecnologia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.usuario')),
            ],
            options={
                'verbose_name_plural': 'Tutoriais',
            },
        ),
        migrations.CreateModel(
            name='Marcacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=10000)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.usuario')),
            ],
            options={
                'verbose_name_plural': 'Marcações',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=500)),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tutorial')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.usuario')),
            ],
            options={
                'verbose_name_plural': 'Comentários',
            },
        ),
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=10000)),
                ('linguagem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tecnologia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.usuario')),
            ],
            options={
                'verbose_name_plural': 'Códigos',
            },
        ),
        migrations.CreateModel(
            name='TutorialConteudo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ordem', models.PositiveIntegerField(blank=True, null=True)),
                ('codigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.codigo')),
                ('marcacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.marcacao')),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tutorial')),
            ],
            options={
                'verbose_name_plural': 'Conteúdos dos Tutoriais',
                'ordering': ['tutorial', 'ordem'],
                'unique_together': {('tutorial', 'ordem')},
            },
        ),
    ]