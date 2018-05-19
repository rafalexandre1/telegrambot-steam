import requests
import json
from telegrambot_steam.configure.config import *
from telegrambot_steam.telegrambot.telegrambot import notifyon
from telegrambot_steam.configure.logconfig import logging


""" 
Onde conseguir a sua "key" da Steam?
https://steamcommunity.com/dev/apikey

"""
key = steam_key()

url_playersumaries = "http://api.steampowered.com/ISteamUser/" \
                     "GetPlayerSummaries/v0002/?key={}&steamids={}"


def main():
    """
    Faz requisição na Api da Steam, verificando se há membros do grupo online,
    se tiver adciona para a lista online[] e envia a mensagem para o grupo
    caso o jogador que está online ficar offline na steam sera removido da
    lista online[]
    """
    online = []
    while True:
        #
        for player in users():
            try:
                req = requests.get(url_playersumaries.format(key, player))
                profile = json.loads(req.text)['response']['players'][0]
                playgame = profile.get('gameextrainfo')
                if playgame != None:
                    if profile['steamid'] not in online:
                        online.append(profile['steamid'])
                        """ENVIAR MENSAGEM DE JOGADOR ONLINE"""
                        try:
                            notifyon(profile['personaname'],
                                     profile['gameextrainfo'])
                        except Exception as msg:
                            logging.error(msg)
                            pass
                    else:
                        pass
            except Exception as log1:
                logging.warning(log1)
                pass

            #
        for player in online:
            try:
                req = requests.get(url_playersumaries.format(key, player))
                profile = json.loads(req.text)['response']['players'][0]
                playgame = profile.get('gameextrainfo')
                if playgame == None:
                    online.remove(player)
                    # ENVIAR MENSAGEM DE JOGADOR OFFLINE
            except Exception as log2:
                logging.warning(log2)
                pass


main()
