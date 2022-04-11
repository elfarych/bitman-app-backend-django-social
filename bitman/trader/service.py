from django_filters import rest_framework as filters
from . import models


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ForecastsFilter(filters.FilterSet):
    symbol = CharFilterInFilter(field_name='symbol')
    title = CharFilterInFilter(field_name='title', lookup_expr='in')

    class Meta:
        model = models.Forecast
        fields = ['symbol', 'title']


class ChatMessagesFilter(filters.FilterSet):
    symbol = CharFilterInFilter(field_name='symbol')

    class Meta:
        model = models.Forecast
        fields = ['symbol']