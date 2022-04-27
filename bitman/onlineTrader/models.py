from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField
from . import service

class TradeSignal(models.Model):
    token = models.CharField(max_length=50, null=True, blank=True)
    order_type = models.CharField(max_length=255, null=True, blank=True) 
    take_profit = models.CharField(max_length=100, null=True, blank=True)
    stop_loss = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(max_length=1000, null=True, blank=True)
    free = models.BooleanField(default=True)
    image = ThumbnailerImageField(upload_to='trade-signals/', resize_source={'size': (1500, 1500), 'crop': 'scale'}, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token

    def save(self, *args, **kwargs):
        service.tg_send_signal(self)

    class Meta:
        ordering = ('-date',)


class CopyTradeResult(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    link_text = models.CharField(max_length=70, null=True, blank=True)
    public = models.BooleanField(default=True)
    file = models.FileField(upload_to='trade-signals-files/', null=True, blank=True)
    image = ThumbnailerImageField(upload_to='trade-signals/', resize_source={'size': (1500, 1500), 'crop': 'scale'}, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)


class TelegramBot(models.Model):
    title = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=50)
    free = models.BooleanField(default=True)

    def __str__(self):
        return self.title
