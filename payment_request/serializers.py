# serializers.py
from rest_framework import serializers
from .models import PaymentInfo

class PaymentSerializer(serializers.ModelSerializer):
    card_cvv = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = PaymentInfo
        fields = '__all__'

