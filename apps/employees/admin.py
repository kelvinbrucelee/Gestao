from django.contrib import admin
from .models import Employee


admin.site.register(Employee)
##@admin.register(Employee)
##class EmployeeAdmin(admin.ModelAdmin):
