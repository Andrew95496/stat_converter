import os
import configparser
import json


config = configparser.ConfigParser()
config.read(
    '/Users/drewskikatana/Documents/Programming/jiu_jistics/void/configs/configs.cfg')

LOG_DIR = config['STAT LOGGER']['LOG_DIR']
FILE_NAME = config['STAT LOGGER']['FILE_NAME']


class LOGGER():

    def __init__(self, athlete, log_dir = LOG_DIR, file_name = FILE_NAME) -> None:
        self.athlete = athlete
        self.log_dir = log_dir
        self.file_name = file_name

    def log(self, logs):
        with open(f'/Users/drewskikatana/Documents/Programming/jiu_jistics/{self.log_dir}{self.athlete}{self.file_name}', 'a+') as logger:
            logger.write(f'{logs}\n')