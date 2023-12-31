# Generated by Django 5.0 on 2023-12-14 20:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('surname', models.CharField(max_length=100, verbose_name='Apellido')),
                ('card_number', models.FloatField(validators=[django.core.validators.MinLengthValidator(limit_value=16)], verbose_name='Numero de tarjeta')),
                ('card_cvv', models.IntegerField(validators=[django.core.validators.MinLengthValidator(limit_value=3), django.core.validators.MaxLengthValidator(limit_value=3)], verbose_name='Clave de tarjeta')),
                ('total_value', models.IntegerField(verbose_name='Total a pagar')),
                ('extra_description', models.TextField(blank=True, null=True, verbose_name='Información adicional')),
            ],
        ),
    ]
