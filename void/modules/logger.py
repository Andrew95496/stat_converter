import configparser
# import json





class LOGGER():

    config: configparser = configparser.ConfigParser()
    config.read(
    '/Users/drewskikatana/Documents/Programming/jiu_jistics/void/configs/configs.cfg')
    LOG_DIR = config['STAT LOGGER']['LOG_DIR']
    FILE_NAME = config['STAT LOGGER']['FILE_NAME']

    __slots__: tuple = ('athlete', 'log_dir', 'file_name')

    def __init__(self, athlete: str, log_dir: str = LOG_DIR, file_name: str = FILE_NAME) -> None:
        self.athlete = athlete
        self.log_dir = log_dir
        self.file_name = file_name


    def log(self, logs, msg=None) -> None:
        with open(f'/Users/drewskikatana/Documents/Programming/jiu_jistics{self.log_dir}{self.athlete}{self.file_name}.log', 'a+') as logger:
            if msg:
                logger.write(f'\n{logs}: {msg}\n')
            else:
                logger.write(f'\n{logs}\n')
