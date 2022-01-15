from django.db import models


class Company(models.Model):
    name = models.CharField('Nome', max_length=100, help_text="Nome da Empresa")


    def __str__(self) -> str:
        return self.name
