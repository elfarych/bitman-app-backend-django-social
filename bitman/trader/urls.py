from django.urls import path
from . import views

urlpatterns = [
    path('trader/me/', views.TraderView.as_view()),
    path('trader/create/', views.TraderCreateView.as_view()),
    path('trader/update/', views.TraderUpdateView.as_view()),
    path('trader/delete/', views.TraderDeleteView.as_view()),


    path('chat/messages/', views.ChatMessagesView.as_view()),
    path('chat/message/create/', views.CreateChatMessage.as_view()),

    path('forecasts/', views.ForecastsListView.as_view()),
    path('forecasts/<int:pk>/', views.ForecastDetailView.as_view()),
    path('forecasts/my/', views.ForecastsListByTraderView.as_view()),
    path('forecasts/create/', views.CreateForecastView.as_view()),
    path('forecasts/delete/<int:pk>/', views.CreateForecastView.as_view()),
]
