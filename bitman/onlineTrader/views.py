from django.shortcuts import render
from rest_framework import generics

from . import serializers
from . import models


class TradeSignalsListView(generics.ListAPIView):
    serializer_class = serializers.TradeSignalSerializer
    queryset = models.TradeSignal.objects.all()


class CopyTradeResultsListView(generics.ListAPIView):
    serializer_class = serializers.CopyTradeResultSerializer
    queryset = models.CopyTradeResult.objects.filter(public=True)
