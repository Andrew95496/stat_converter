import os
import configparser
import json



config = configparser.ConfigParser()
config.read(f'{os.getcwd()}/void/configs/configs.cfg')
LOGDIR = config['STAT LOGGER']['LOGDIR']

class StatLogger():

    def __init__(self, flags) -> None:
        with open('void/test/test_logger/flag_log.txt', 'a+') as file:
            file.write(f'{flags}\n')



    