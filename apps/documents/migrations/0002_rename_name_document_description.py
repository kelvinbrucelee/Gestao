# Generated by Django 4.0.1 on 2022-01-15 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='name',
            new_name='description',
        ),
    ]
