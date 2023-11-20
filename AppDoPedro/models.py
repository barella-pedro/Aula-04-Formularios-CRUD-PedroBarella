from django.db import models

class Jogadores(models.Model):
  nome_jogador = models.CharField(max_length=50)
  feito_historico = models.CharField(max_length=200)
  pontos_totais = models.PositiveIntegerField()
  colocacao_pts = models.CharField(max_length=50)
  info_titulos = models.CharField(max_length=200)
  media_pts = models.FloatField()
  media_assist = models.FloatField()
  media_rebs = models.FloatField()

class Usuario(models.Model):
  nome_usuario = models.CharField(max_length=50)
  time = models.CharField(max_length=50)
  top1 = models.ManyToManyField(Jogadores, related_name='top1', blank=True)
  top2 = models.ManyToManyField(Jogadores, related_name='top2', blank=True)
  top3 = models.ManyToManyField(Jogadores, related_name='top3', blank=True)
  
class Userlist(models.Model):
  top1 = models.CharField(max_length=50)
  top2 = models.CharField(max_length=50)
  top3 = models.CharField(max_length=50)
  time = models.CharField(max_length=50)
  usuario_nome = models.CharField(max_length=50, default=None, null=True, blank=True)