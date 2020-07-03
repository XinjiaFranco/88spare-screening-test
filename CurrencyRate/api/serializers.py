from rest_framework import serializers
from .models import CurrencyData


class CurrencyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyData
        fields = ['id', 'currency', 'value', 'rate']

