from re import M
from django.db import models


class Department(models.Model):
    name = models.CharField('Nome',max_length=100)


    class Meta:
        verbose_name_plural = 'DEPARTAMENTOS'
        ordering = ("id",)


    def __str__(self) -> str:
        return self.name
