import imp
from django.db import models
from apps.employees.models import Employee


class Document(models.Model):
    description = models.CharField(max_length=100)
    belongs = models.ForeignKey(Employee, on_delete=models.PROTECT)


    class Meta:
        verbose_name_plural = 'DOCUMENTOS'
        ordering = ("id",)



    def __str__(self) -> str:
        return self.description
