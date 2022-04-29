import re
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import service


class TraderView(generics.ListAPIView):
    """Get trader by user"""
    serializer_class = serializers.TraderSerializer

    def get_queryset(self):
        trader = models.Trader.objects.filter(user=self.request.user)
        return trader


class TraderCreateView(generics.CreateAPIView):
    """Create trader profile"""
    queryset = models.Trader.objects.all()
    serializer_class = serializers.TraderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TraderUpdateView(generics.UpdateAPIView):
    """Update trader profile"""
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = serializers.TraderSerializer

    def get_queryset(self):
        trader = models.Trader.objects.filter(user=self.request.user)
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
    filter_backends = [DjangoFilterBackend]
    filterset_class = service.ChatMessagesFilter


class CreateChatMessage(generics.CreateAPIView):
    """Create chat message"""
    queryset = models.ChatMessage.objects.all()
    serializer_class = serializers.ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        trader = models.Trader.objects.find_by_user(self.request.user)
        serializer.save(trader=trader)


class ForecastDeleteView(generics.DestroyAPIView):
    """Delete forecast"""
    serializer_class = serializers.ForecastDetailSerializer

    def get_queryset(self):
        trader = models.Trader.objects.find_by_user(self.request.user)
        forecasts = models.Forecast.objects.filter(trader=trader)
        return forecasts


class CreateCaseView(generics.CreateAPIView):
    """Create new trader case view"""
    serializer_class = serializers.CaseSerializer
    queryset = models.Case.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        trader = models.Trader.objects.filter(user=user)[0]
        serializer.save(trader=trader, user=user)


class UpdateCaseView(generics.UpdateAPIView):
    """Update trader case by id"""
    serializer_class = serializers.CaseSerializer

    def get_queryset(self):
        cases = models.Case.objects.filter(user=self.request.user)
        return cases


class DeleteCaseView(generics.DestroyAPIView):
    """Delete case by id"""
    serializer_class = serializers.CaseSerializer

    def get_queryset(self):
        cases = models.Case.objects.filter(user=self.request.user)
        return cases


class CreateCaseTokenView(generics.CreateAPIView):
    """Create case token"""
    serializer_class = serializers.CaseTokenSerializer
    queryset = models.CaseToken.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateCaseTokenView(generics.UpdateAPIView):
    """Update case token"""
    serializer_class = serializers.CaseTokenSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        case_tokens = models.CaseToken.objects.filter(user=self.request.user)
        return case_tokens


class DeleteCaseTokenView(generics.DestroyAPIView):
    """Delete case token by id"""
    serializer_class = serializers.CaseTokenSerializer

    def get_queryset(self):
        cases = models.CaseToken.objects.filter(user=self.request.user)
        return cases


class CreateCaseTokenOrderView(generics.CreateAPIView):
    """Create case token order"""
    serializer_class = serializers.CaseTokenOrderSerializer
    queryset = models.CaseTokenOrder.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateCaseTokenOrderView(generics.UpdateAPIView):
    """Update case token order"""
    serializer_class = serializers.CaseTokenOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        fixed_case_items = models.CaseTokenOrder.objects.filter(user=self.request.user)
        return fixed_case_items


class DeleteCaseTokenOrderView(generics.UpdateAPIView):
    """Delete case token order"""
    serializer_class = serializers.CaseTokenOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        fixed_case_items = models.CaseTokenOrder.objects.filter(user=self.request.user)
        return fixed_case_items
