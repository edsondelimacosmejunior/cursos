# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-08 01:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfis', '0003_perfil_contatos'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
