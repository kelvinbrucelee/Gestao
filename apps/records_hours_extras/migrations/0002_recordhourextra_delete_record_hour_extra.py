# Generated by Django 4.0.1 on 2022-01-15 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records_hours_extras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordHourExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=100, verbose_name='Motivo')),
            ],
        ),
        migrations.DeleteModel(
            name='Record_hour_extra',
        ),
    ]
