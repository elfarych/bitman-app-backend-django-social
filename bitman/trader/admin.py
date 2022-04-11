from django.contrib import admin
from . import models


class WathListInline(admin.TabularInline):
    model = models.WatchList
    extra = 0


class SettingInline(admin.TabularInline):
    model = models.Setting
    extra = 0


class ChatMessageInline(admin.TabularInline):
    model = models.ChatMessage
    extra = 0


class CaseInline(admin.TabularInline):
    model = models.Case
    extra = 0


@admin.register(models.Trader)
class TraderAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'email', 'chat_banned', 'date', 'update')
    search_fields = ('user__username', 'name', 'email')
    list_filter = ('chat_banned', 'date', 'update')
    inlines = [WathListInline, SettingInline, ChatMessageInline, CaseInline]


@admin.register(models.WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('trader', 'date', 'update')
    search_fields = ('trader__user__username', 'symbols')
    list_filter = ('date', 'update')


@admin.register(models.ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('trader', 'symbol', 'date', 'update')
    search_fields = ('trader__user__username', 'symbol', 'text')
    list_filter = ('date', 'update')


class CaseItemInline(admin.TabularInline):
    model = models.CaseItem
    extra = 0


@admin.register(models.Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('trader', 'title', 'date', 'update')
    search_fields = ('trader__user__username', 'title')
    list_filter = ('date', 'update')
    inlines = [CaseItemInline]


class ForecastImagesInlines(admin.TabularInline):
    model = models.ForecastImages
    extra = 0


@admin.register(models.Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('title', 'symbol', 'trader', 'date', 'update')
    search_fields = ('trader__user__username', 'symbol', 'title', 'symbol')
    list_filter = ('date', 'update',  'symbol')
    inlines = [ForecastImagesInlines]
