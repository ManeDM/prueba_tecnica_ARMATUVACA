from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver

class PaymentInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre', null=False)
    surname = models.CharField(max_length=100, verbose_name='Apellido', null=False)
    card_number = models.CharField(max_length=16, verbose_name='Numero de tarjeta', null=False)
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
        
        comission_percentage = 0.03  
        iva_percentage = 0.0199  
        retencion_percentage = 0.015  

        comission_value = self.total_value * comission_percentage
        iva_value = comission_value * iva_percentage
        retencion_value = self.total_value * retencion_percentage

        total_comission = comission_value + iva_value + retencion_value
        return total_comission

@receiver(pre_save, sender=PaymentInfo)
def hide_card_number(sender, instance, **kwargs):
    
    card_number_str = str(instance.card_number)
    hidden_digits = '*' * (len(card_number_str) - 4)
    visible_digits = card_number_str[-4:]
    transformed_card_number = hidden_digits + visible_digits
    instance.card_number = transformed_card_number


    instance.comission_value = instance.calculate_comission()