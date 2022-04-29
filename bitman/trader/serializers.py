from rest_framework import serializers
from . import models


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Setting
        fields = ('json',)


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WatchList
        fields = '__all__'


class CaseTokenOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CaseTokenOrder
        fields = '__all__'


class CaseTokenSerializer(serializers.ModelSerializer):
    orders = CaseTokenOrderSerializer(many=True, read_only=True)

    class Meta:
        model = models.CaseToken
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):
    tokens = CaseTokenSerializer(many=True, read_only=True)
    token_orders = CaseTokenOrderSerializer(many=True, read_only=True)

    class Meta:
        model = models.Case
        fields = '__all__'


class ReferalTraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Trader
        fields = '__all__'


class TraderSerializer(serializers.ModelSerializer):
    
    watchlist = WatchListSerializer(many=False, read_only=True)
    setting = SettingSerializer(many=False, read_only=True)
    cases = CaseSerializer(many=True, read_only=True)
    referals = ReferalTraderSerializer(many=True, read_only=True)

    class Meta:
        model = models.Trader
        fields = '__all__'


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChatMessage
        fields = '__all__'


class ForecastListSerializer(serializers.ModelSerializer):

    trader = TraderSerializer(many=False, read_only=True)

    class Meta:
        model = models.Forecast
        fields = ('id', 'title', 'image', 'trader', 'description', 'symbol', 'date', 'update')


class ForecastImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ForecastImages
        fields = ('image',)


class ForecastDetailSerializer(serializers.ModelSerializer):

    images = ForecastImageSerializer(many=True, read_only=True)
    trader = TraderSerializer(many=False, read_only=True)

    class Meta:
        model = models.Forecast
        fields = '__all__'





