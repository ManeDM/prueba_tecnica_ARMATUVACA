from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class PaymentInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre', null=False)
    surname = models.CharField(max_length=100, verbose_name='Apellido', null=False)
    card_number = models.IntegerField(max_length=16, verbose_name='Numero de tarjeta', null=False)
    card_cvv = models.IntegerField(validators=[MinLengthValidator(limit_value=3), MaxLengthValidator(limit_value=3)], verbose_name='Clave de tarjeta', null=True, blank=True)
    total_value = models.IntegerField(verbose_name='Total a pagar', null=False)
    extra_description = models.TextField(blank=True, null=True, verbose_name='Información adicional')
    comission_value = models.FloatField(null=True, blank=True, verbose_name='Comisión')

    def save(self, *args, **kwargs):
        card_cvv = self.card_cvv
        self.card_cvv = None

        self.comission_value = self.calculate_comission()

        super().save(*args, **kwargs)

        self.card_cvv = card_cvv

    def calculate_comission(self):
        
        comission_percentage = 0.03  # 3%
        iva_percentage = 0.0199  # 1.99%
        retencion_percentage = 0.015  # 1.5%

        comission_value = self.total_value * comission_percentage
        iva_value = comission_value * iva_percentage
        retencion_value = self.total_value * retencion_percentage

        total_comission = comission_value + iva_value + retencion_value
        return total_comission