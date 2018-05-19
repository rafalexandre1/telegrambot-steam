from telegram import Bot, ParseMode
from telegram.ext import Updater
from telegrambot_steam.configure.config import chat_id, telegram_token
from telegrambot_steam.configure.logconfig import logging


bot = Bot(telegram_token())
updater = Updater(telegram_token())
dispatcher = updater.dispatcher

# Mensagem a ser enviada pelo Bot
MSG_ON = "👤 _Player:_ *{}* \n" \
         "ℹ️️ _Status:_ `{}` \n" \
         "🕹 _Game:_ *{}* \n"


def notifyon(personaname, gameextrainfo):
    """
    Envia a mensagem no Telegram

    :param personaname: Nome do usuário
    :param gameextrainfo: Nome do Game
    """
    try:
        bot.send_message(chat_id=chat_id(),
                         text=MSG_ON.format(personaname, 'online', gameextrainfo),
                         parse_mode=ParseMode.MARKDOWN)
    except Exception as log:
        logging.error(log)
        pass
