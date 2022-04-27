import imp
from rest_framework import serializers
from . import models


class TradeSignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TradeSignal
        fields = '__all__'


class CopyTradeResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CopyTradeResult
        fields = '__all__'
