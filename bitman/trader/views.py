import re
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from . import models
from . import service


class TraderView(generics.RetrieveAPIView):
    """Get trader by user"""
    serializer_class = serializers.TraderSerializer

    def get_queryset(self):
        trader = models.Trader.objects.find_by_user(self.request.user)    
        return trader


class TraderCreateView(generics.CreateAPIView):
    """Create trader profile"""
    queryset = models.Trader.objects.all()
    serializer_class = serializers.TraderSerializer


class TraderUpdateView(generics.UpdateAPIView):
    """Update trader profile"""
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = serializers.TraderSerializer

    def get_queryset(self):
        trader = models.Trader.objects.find_by_user(self.request.user)    
        return trader


class TraderDeleteView(generics.DestroyAPIView):
    """Delete trader profile"""
    serializer_class = serializers.TraderSerializer

    def get_queryset(self):
        trader = models.Trader.objects.find_by_user(self.request.user)    
        return trader


class ChatMessagesView(generics.ListAPIView):
    """Get chat messages by symbol (query)"""
    serializer_class = serializers.ChatMessageSerializer

    def get_queryset(self):
        messages = models.ChatMessage.objects.filter(symbol=self.kwargs['symbol']))    
        return messages


class CreateChatMessage(generics.CreateAPIView):
    """Create chat message"""
    queryset = models.ChatMessage.objects.all()
    serializer_class = serializers.ChatMessageSerializer


class ForecastsListView(generics.ListAPIView):
    """Get forecast list"""
    queryset = models.Forecast.objects.filter(public=True)
    serializer_class = serializers.ForecastListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = service.ForecastsFilter


class ForecastsListByTraderView(generics.ListAPIView):
    """Get forecast list by trader"""
    serializer_class = serializers.ForecastListSerializer

    def get_queryset(self):
        trader = models.Trader.objects.find_by_user(self.request.user)   
        forecasts = models.Forecast.objects.filter(trader=trader) 
        return forecasts


class ForecastDetailView(generics.RetrieveAPIView):
    """Get forecast detail by id"""
    forecasts = models.Forecast.objects.filter(public=True) 
    serializer_class = serializers.ForecastDetailSerializer


class CreateForecastView(generics.CreateAPIView):
    """Create forecast"""
    queryset = models.Forecast.objects.all()
    serializer_class = serializers.ForecastDetailSerializer

    def perform_create(self, serializer):
        trader = models.Trader.objects.find_by_user(self.request.user)
        serializer.save(trader=trader)


class ForecastDeleteView(generics.DestroyAPIView):
    """Delete Forecast"""
    queryset = models.Forecast.objects.all()
    serializer_class = serializers.ForecastDetailSerializer
