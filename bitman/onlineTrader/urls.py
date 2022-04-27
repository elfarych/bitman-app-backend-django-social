from django.urls import path
from . import views


urlpatterns = [
    path('trade_siglnals/', views.TradeSignalsListView.as_view()),
    path('copy_trade_results/', views.CopyTradeResultsListView.as_view()),
]