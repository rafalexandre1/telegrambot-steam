#!/bin/sh

python3.6 setup.py install

chmod +x python_init.py start-bot.sh

exit
#&& sudo chown $USER:$USER python_init.py start-bot.sh