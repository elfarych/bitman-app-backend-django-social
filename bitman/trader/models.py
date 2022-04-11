from operator import mod
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Trader(models.Model):
    # Пользователь
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(null=True, blank=True)
    avatar = ThumbnailerImageField(upload_to='users/', resize_source={'size': (500, 500), 'crop': 'scale'})
    chat_banned = models.BooleanField(default=False)
    invite_id = models.PositiveIntegerField(null=True, blank=True) 
    for_referals_paid_sum = models.PositiveIntegerField(default=0)
    referals = models.ManyToManyField('self', related_name='referals', symmetrical=False)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.user.username

    class Meta:
        ordering = ('-date',)


class WatchList(models.Model):
    # Список избранного
    trader = models.OneToOneField(Trader, on_delete=models.SET_NULL, null=True, blank=True, related_name='watchlist')
    symbols = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.title}'

    class Meta:
        ordering = ('order', '-date')


class ChatMessage(models.Model):
    # Сообщения в чате
    trader = models.ForeignKey(Trader, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    answer_for = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='answers')
    symbol = models.CharField(max_length=20, null=True, blank=True, db_index=True)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.trader

    class Meta:
        ordering = ('-date',)


class Setting(models.Model):
    # Настройки пользователя
    trader = models.OneToOneField(Trader, on_delete=models.CASCADE, related_name="settings")
    json = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.trader


class Case(models.Model):
    # Портфель
    trader = models.ForeignKey(Trader, on_delete=models.SET_NULL, null=True, blank=True, related_name='cases')
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255, null=True, blank=True)
    public = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'${self.trader} - ${self.symbol}'

    class Meta:
        ordering = ('-date',)   


class CaseItem(models.Model):
    # Монета в портфеле
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='items')
    symbol = models.CharField(max_length=20)
    price = models.FloatField()
    quantity_usd = models.FloatField()
    quantity_base_asset = models.FloatField()
    sum_usd = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'${self.case} - ${self.symbol}'

    class Meta:
        ordering = ('-date',)


class Forecast(models.Model):
    # Прогноз
    trader = models.ForeignKey(Trader, on_delete=models.SET_NULL, null=True, blank=True, related_name='forecasts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    symbol = models.CharField(max_length=20)
    image = ThumbnailerImageField(upload_to='forecasts/', resize_source={'size': (1300, 1300), 'crop': 'scale'})
    content = RichTextUploadingField()
    public = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)


class ForecastImages(models.Model):
    # Картинки прогноза
    forecast = models.ForeignKey(Forecast, on_delete=models.CASCADE, related_name='images')
    image = ThumbnailerImageField(upload_to='forecasts/', resize_source={'size': (1300, 1300), 'crop': 'scale'})
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.forecast
    
    class Meta:
        ordering = ('-date',)