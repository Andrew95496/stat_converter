import os
import configparser
import json


def __update_config__():
    config = configparser.ConfigParser()
    config.read(f'{os.getcwd()}/void/configs/configs.cfg')
    athlete_xlsx_file = []
    temp = os.listdir(
        '/Users/drewskikatana/Documents/Programming/jiu_jistics/void/TEST/test_excel_files_import/')
    defaults = config['DEFAULTS']
    for athlete in temp:
            new = athlete.removesuffix('.xlsx')
            athlete_xlsx_file.append(new)
    athlete_xlsx_file_string = json.dumps(athlete_xlsx_file)
    defaults['ATHLETES'] = str(athlete_xlsx_file_string)

    with open(f'{os.getcwd()}/void/configs/configs.cfg', 'w') as cfg:
        config.write(cfg)

