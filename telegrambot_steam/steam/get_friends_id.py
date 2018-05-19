"""
Execute este script para obter o STEAM ID dos amigos

"""

import requests
import json
from telegrambot_steam.configure.config import steam_key
from telegrambot_steam.configure.logconfig import logging


url_friendlist = "http://api.steampowered.com/ISteamUser/GetFriendList/" \
                 "v0001/?key={}&steamid={}&relationship=friend"

url_playersummaries = "http://api.steampowered.com/ISteamUser/" \
                      "GetPlayerSummaries/v0002/?key={}&steamids={}"


def get_steam_key():
    """
    Salvar a Steam Key
    """
    file = open("telegrambot_steam/steam/key.txt", "w")
    steamkey = input("\n\n\033[1mDigite sua Steam Key:\033[m ")
    file.write(steamkey)
    file.close()
    file1 = open("telegrambot_steam/steam/key.txt", "r")
    file1.close()


def getfriendlist(steam_id):
    """
    Faz requisição na API da Steam
    Retorna um dicionário com os Steam Id dos Amigos do usuário
    """

    friendlist = []
    try:
        req = requests.get(url_friendlist.format(steam_key(), steam_id))
        friends_id = json.loads(req.text)

        for player in friends_id['friendslist']['friends']:
            friendlist.append(player['steamid'])

    except Exception as log:
        logging.warning(log)

        # ARRUMAR ISSO
        print('Ops...\nOuve um erro')
        quit()
    return friendlist


def getplayersummaries(steam_id):
    """
    Faz requisição na API da Steam
    Retorna nome de usuário e o Steam ID
    """
    try:
        req = requests.get(url_playersummaries.format(steam_key(), steam_id))
        profile = json.loads(req.text)
        username = profile['response']['players'][0]['personaname']
        id_ = profile['response']['players'][0]['steamid']

    except Exception as log:
        logging.warning(log)

        username = None
        id_ = None
        print('\033[1;31mSteam Id incorreto, tente novamente.\033[m')
        quit()
    return username, id_


def friends_steam(steamid):
    """
    Retorna as os nomes de usuários e Steam Ids dos amigos na tela
    """
    print(
        'username: {:20}   steam_id: \033[1;32m{}\033[m'.format(
            getplayersummaries(steamid)[0], getplayersummaries(steamid)[1]
        )
    )
    for player in getfriendlist(steamid):
        print(
            'username: {:20}   steam_id: \033[1;32m{}\033[m'.format(
                getplayersummaries(player)[0], getplayersummaries(player)[1]
            )
        )


def get_steam_ids():
    """
    Saida na tela das Steam Ids dos amigos
    """
    print('\n\033[1mVocê pode conseguir o Steam Id na URL do seu perfil '
          'da Steam\033[m')
    steamid = input('\033[1mInforme seu Steam Id:\033[m ')

    print('\n')
    friends_steam(steamid)
    print('\n\n\033[1;33mColoque os Steam Ids que deseja no arquivo\n'
          'telegrambot_steam/steam/steam_ids.txt\033[m\n')


execute = None
get_steam_key()
get_steam_ids()
