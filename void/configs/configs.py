import os
import configparser
import json

from .update_method import __update_config__

class Config():
    __update_config__()

    config = configparser.ConfigParser()
    config.read(f'{os.getcwd()}/void/configs/configs.cfg')
    
    # VOID configs
    IMPORT_DIR = config['DEFAULTS']['IMPORT_DIR']
    EXPORT_DIR = config['DEFAULTS']['EXPORT_DIR']
    ATHLETES = json.loads(config.get("DEFAULTS", "ATHLETES"))
    SHEET_NAME = config['DEFAULTS']['SHEET_NAME']


    def __init__(self, ROOT_DIR: str =f"{os.getcwd()}/athletes/", IMPORT_DIR: str = IMPORT_DIR, EXPORT_DIR: str = EXPORT_DIR, ATHLETES: list[str] = ATHLETES, SHEET_NAME: str = SHEET_NAME) -> None:
        self.ROOT_DIR = ROOT_DIR
        self.IMPORT_DIR = IMPORT_DIR
        self.EXPORT_DIR = EXPORT_DIR
        self.ATHLETES = ATHLETES
        self.SHEET_NAME = SHEET_NAME

   
    

if __name__ == '__main__':

    conf = Config()


    # for athlete in conf.ATHLETES:
    #     print(f'{conf.IMPORT_DIR}{athlete}')
    #     print('SHEET NAME:',f'{athlete}{conf.SHEET_NAME}')