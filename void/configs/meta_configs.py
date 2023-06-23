import os
import configparser
import json


# * Home directory path
# print(os.path.expanduser('~'))

# TODO: revert default settings
# TODO: What if import dir is empty or doesn't exist

class Configs():

    @staticmethod
    def __load__(config):
        with open(f'{os.getcwd()}/void/configs/configs.cfg', 'w') as cfg:
            config.write(cfg)

    @staticmethod
    def __default__():
        config = configparser.ConfigParser()
        config.read(f'{os.getcwd()}/void/configs/configs.cfg')

        config.add_section('DEFAULTS')
        config.set('root_dir')
        config.set('import_dir')
        config.set('export_dir')
        config.set('athletes')
        config.set('sheet_name')

        config.add_section('STAT LOGGER')
        config.set('log_dir')
        config.set('file_name')

        Configs.__load__(config)




    @staticmethod
    def __update__():
        print('ran update')
        home = os.path.expanduser('~')
        config = configparser.ConfigParser()
        config.read(f'{os.getcwd()}/void/configs/configs.cfg')

        try:
            temp = os.listdir(f'{home}/Documents/Programming/jiu_jistics/void/TEST/test_excel_files_import/')
        except FileNotFoundError:
            temp = os.mkdir(f'{home}/Documents/Programming/jiu_jistics/void/TEST/test_excel_files_import/')
        
        try:
            athlete_xlsx_file = [athlete.removesuffix('.xlsx') for athlete in temp]
            defaults = config['DEFAULTS']
            defaults['ATHLETES'] = json.dumps(athlete_xlsx_file)
            if len(athlete_xlsx_file) == 0:
                print('WARNING: import directory is empty')
        except KeyError:
            print('XXXXXXX')
            Configs.__default__()
            create_cfg = open('/void/configs/configs.cfg', 'r')
            create_cfg.close()
            athlete_xlsx_file = [athlete.removesuffix(
                '.xlsx') for athlete in temp]
            defaults = config['DEFAULTS']
            defaults['ATHLETES'] = json.dumps(athlete_xlsx_file)
            if len(athlete_xlsx_file) == 0:
                print('WARNING: import directory is empty')

        Configs.__load__(config)
            

        

    

