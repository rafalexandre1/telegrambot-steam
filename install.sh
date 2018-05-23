#!/bin/sh

sudo pip3 install -r requirements.txt
sudo python3 setup.py install

sudo chmod +x python_init.py start-bot.sh
sudo chown $USER:$USER python_init.py start-bot.sh

exit
