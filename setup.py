from setuptools import setup
import os

# Setup e instalação de bibliotecas extras
setup(name='telegrambot-steam',
      version='0.1',
      author='Rafael Alexandre',
      author_email='rafael.alexandre.tm@gmail.com',
      url='https://github.com/rafael-alexandre13',
      # install_requires=['python-telegrambot-bot',
      #                   'requests'])
      )


os.system("sudo pip install -r requirements.txt")

# CONFIGURAÇÔES INICIAIS
from telegrambot_steam.steam import get_friends_id
from telegrambot_steam.telegrambot import get_telegram_config
from telegrambot_steam.configure.config import create_start

create_start()
a = get_friends_id.execute
b = get_telegram_config.execute
