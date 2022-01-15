from django.db import models


class Company(models.Model):
    name = models.CharField('Nome', max_length=100, help_text="Nome da Empresa")

    class Meta:
        verbose_name_plural = 'EMPRESAS'
        ordering = ("id",)


    def __str__(self) -> str:
        return self.name
