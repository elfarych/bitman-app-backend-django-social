from django.urls import path
from . import views

urlpatterns = [
    path('trader/me/', views.TraderView.as_view()),
    path('trader/create/', views.TraderCreateView.as_view()),
    path('trader/update/<int:pk>/', views.TraderUpdateView.as_view()),
    path('trader/delete/', views.TraderDeleteView.as_view()),


    path('chat/messages/', views.ChatMessagesView.as_view()),
    path('chat/message/create/', views.CreateChatMessage.as_view()),

    path('case/', views.CaseListView.as_view()),
    path('case/create/', views.CreateCaseView.as_view()),
    path('case/update/<int:pk>/', views.UpdateCaseView.as_view()),
    path('case/delete/<int:pk>/', views.DeleteCaseView.as_view()),

    path('case_token/create/', views.CreateCaseTokenView.as_view()),
    path('case_token/update/<int:pk>/', views.UpdateCaseTokenView.as_view()),
    path('case_token/delete/<int:pk>/', views.DeleteCaseTokenView.as_view()),

    path('case_token_order/create/', views.CreateCaseTokenOrderView.as_view()),
    path('case_token_order/update/<int:pk>/', views.UpdateCaseTokenOrderView.as_view()),
    path('case_token_order/delete/<int:pk>/', views.DeleteCaseTokenView.as_view()),

    path('forecasts/', views.ForecastsListView.as_view()),
    path('forecasts/<int:pk>/', views.ForecastDetailView.as_view()),
    path('forecasts/my/', views.ForecastsListByTraderView.as_view()),
    path('forecasts/create/', views.CreateForecastView.as_view()),
    path('forecasts/delete/<int:pk>/', views.CreateForecastView.as_view()),
]
