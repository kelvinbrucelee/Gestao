# Generated by Django 4.0.1 on 2022-01-15 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('id',), 'verbose_name_plural': 'FUNCIONARIOS'},
        ),
    ]
