from django.contrib import admin
from . import models


@admin.register(models.TradeSignal)
class TradeSignalAdmin(admin.ModelAdmin):
    list_display = ('token', 'order_type', 'free', 'date')
    search_fields = ('token', 'comment', 'email')
    list_filter = ('free', 'token', 'date')


@admin.register(models.CopyTradeResult)
class CopyTradeResultAdmin(admin.ModelAdmin):
    list_display = ('title', 'public', 'date')
    search_fields = ('title',)
    list_filter = ('public', 'date')


@admin.register(models.TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


