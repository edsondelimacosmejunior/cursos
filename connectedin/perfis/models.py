# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Perfil(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False
    )

    empresa = models.CharField(
        max_length=255,
        null=False
    )


    def convidar(self, perfil_convidado):
        Convite(solicitante=self, convidado=perfil_convidado).save()


class Convite(models.Model):

    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')