import telebot
from . import models


def tg_send_signal(signal):
    bots = models.TelegramBot.objects.all()
    if bots:
        for i in bots:
            if i.free == signal.free:
                bot = telebot.TeleBot(i.key)
                chat_id = i.chat_id

                if (signal.image):
                    try:
                        bot.send_photo(chat_id, signal.image, caption=get_text(signal))
                    except:
                        return
                
                else:
                    try:
                        bot.send_message(chat_id, text=get_text(signal))
                    except:
                        return


def get_text(signal):
    text = f'#{signal.token} \n \
{signal.order_type} \n \
TP: {signal.take_profit} \n \
SL: {signal.stop_loss} \n\n \
{signal.comment}'

    return text