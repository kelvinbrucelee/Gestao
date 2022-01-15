from django.db import models
from apps.employees.models import Employee


class RecordHourExtra(models.Model):
    reason = models.CharField('Motivo', max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)


    class Meta:
        verbose_name_plural = 'REGISTRO DE HORAS EXTRAS'
        ordering = ("id",)



    def __str__(self) -> str:
        return self.reason
