from django.db import models


class company(models.Model):
    name = models.CharField(max_length=100, help_text="Nome da Empresa")
