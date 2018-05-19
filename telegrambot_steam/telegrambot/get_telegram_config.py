"""
Execute este script para obter o CHAT_ID do Telegram

"""

from telegram.ext import Updater, CommandHandler
from telegram import Bot
from telegrambot_steam.configure.config import telegram_token
import os


def get_token():
    """
    Salvar o token.txt do Bot.
    """
    file = open("telegrambot_steam/telegrambot/token.txt", "w")
    token = input("\n\n\033[1mDigite o Token do Bot:\033[m ")
    file.write(token)
    file.close()


execute = None
get_token()

bot = Bot(telegram_token())
updater = Updater(telegram_token())
dispatcher = updater.dispatcher


def get_id(bot, update):
    """
    O Bot enviara uma confirmação de que o comando foi recebido,
    assim ele pegará o nome do grupo ou nome de usuário e o chat_id
    e mostrará na linha de comando executado.

    Salvara o chat id em um arquivo.
    """
    bot.send_message(chat_id=update.message.chat_id, text='☑️')
    chatype = update.message['chat']['type']
    chatid = str(update.message['chat']['id'])
    msgchat_id = 'chat_id: \033[1;32m{}\033[m'.format(chatid)

    if chatype == 'group':
        print('Group: {}\n{}\n'.format(update.message['chat']['title'],
                                       msgchat_id))
    elif chatype == 'private':
        print('Username: {}\n{}\n'.format(update.message['chat']['username'],
                                          msgchat_id))

    file = open("telegrambot_steam/telegrambot/chat_id.txt", "w")
    file.write(chatid)
    file.close()
    os._exit(1)


def get_chat_id():
    print('\n\033[1mEnvie o comando \033[34m/steam\033[m\033[1m para o seu '
          'Bot no telegram\033[m\n')

    start_handler = CommandHandler('steam', get_id)
    dispatcher.add_handler(start_handler)

    updater.start_polling()


get_chat_id()
