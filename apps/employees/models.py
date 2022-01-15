from django.contrib.auth.models import User
from django.db import models
from apps.departments.models import Department
from apps.companies.models import Company

class Employee(models.Model):
    name = models.CharField('Nome', max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departments = models.ManyToManyField(Department)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'FUNCIONARIOS'
        ordering = ("id",)


    def __str__(self) -> str:
        return self.name
