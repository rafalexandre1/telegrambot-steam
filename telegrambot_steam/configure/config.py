""" Todas as informações deverão estar entre aspas"""


def telegram_token():
    """
    Token do @Botfather do Telegram
    """
    file = open("telegrambot_steam/telegrambot/token.txt", "r")
    token = file.read()
    file.close()
    return token


def chat_id():
    """
    Id do Chat em que o Bot enviará as notificações
    """
    file = open("telegrambot_steam/telegrambot/chat_id.txt", "r")
    chat = file.read()
    file.close()
    return chat


def steam_key():
    """
    Chave de desenvolvedor da Steam API
    """
    file = open("telegrambot_steam/steam/key.txt", "r")
    key = file.read()
    file.close()
    return key


def users():
    """
    Lista com os Steam Id dos membros do grupo
    """
    userslist = []
    file = open("telegrambot_steam/steam/steam_ids.txt", "r")
    for i in file:
        userslist.append(i.rstrip())

    return userslist


def create_start():
    file = open("python_init.py", "w")
    file.write("from telegrambot_steam import bot_steam\n\n"
               "if __name__ == '__main__':\n    bot_steam.main()\n")
    file.close()

    scriptsh = open("start-bot.sh", "w")
    scriptsh.write("#!/bin/sh\n\npython3 python_init.py")
    scriptsh.close()
