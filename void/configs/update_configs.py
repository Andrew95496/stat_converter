import os
import configparser
import json

# * Home directory path
# print(os.path.expanduser('~'))

# TODO: revert default settings
# TODO: What if import dir is empty or doesn't exist

class UpdateConfigs():

    @staticmethod
    def __update_config__():
        home = os.path.expanduser('~')
        config = configparser.ConfigParser()
        config.read(f'{os.getcwd()}/void/configs/configs.cfg')
        temp = os.listdir(f'{home}/Documents/Programming/jiu_jistics/void/TEST/test_excel_files_import/')
        athlete_xlsx_file = [athlete.removesuffix('.xlsx') for athlete in temp]
        defaults = config['DEFAULTS']
        defaults['ATHLETES'] = json.dumps(athlete_xlsx_file)
        if len(athlete_xlsx_file) == 0:
            print('WARNING: import directory is empty')
        with open(f'{os.getcwd()}/void/configs/configs.cfg', 'w') as cfg:
            config.write(cfg)

    @staticmethod
    def __restore__():
        pass

