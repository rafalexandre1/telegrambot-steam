import logging

""" Configuração dos Logs """

LOGFORMAT = "%(asctime)s : %(levelname)s : %(filename)s : line:%(lineno)d :" \
            " %(message)s\n"

logging.basicConfig(filename='log.log',
                    format=LOGFORMAT,
                    datefmt='%d-%m-%Y  %H:%M:%S')