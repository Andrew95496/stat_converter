import modules
import configs

import os

# load_dir = config['DEFAULTS']['LOAD_DIR']
# athletes = ast.literal_eval(config['DEFAULTS']['ATHLETES'])
# sheet_name = config['DEFAULTS']['SHEET_NAME']


# athlete: str | None = None, opponent: str | None = None, time: list[str] = None
class VOID():

    def __init__(self, import_dir=configs.Config.IMPORT_DIR, sheet_name=configs.Config.SHEET_NAME, athletes: list[str] = configs.Config.ATHLETES, tables: list[dict] | None = None, parsed_stats: list[dict] | None = None) -> None:
        self.import_dir = import_dir
        self.sheet_name = sheet_name
        self.athletes = athletes
        if tables is None:
            self.tables = {}
        if parsed_stats is None:
            self.parsed_stats = {}
        # self.athlete = athlete
        # self.opponent = opponent
        # self.time = time
        os.system('bash saves.sh')



    def get_tables(self):
        for athlete in self.athletes:
            dataframe = modules.FileImporter(
                athlete, f'{athlete}{self.sheet_name}', f'{self.import_dir}{athlete}.xlsx')
            dataframe = dataframe.import_excel()
            self.tables[athlete] = (dataframe)
        return self.tables
    
    def stat_parse(self):
        count = 1
        for athlete, dataframes in self.tables.items():
            athlete = athlete.replace('_', ' ')
            for table in dataframes:
                stats = modules.stat_type.StatType()
                # print(
                #     f'\n{modules.bcolors.BOLD}{modules.bcolors.HEADER}{athlete.capitalize()}{modules.bcolors.ENDC}\n')
                stat_col = stats.assign_type(table['Stats'])
                self.parsed_stats[f'{athlete}_{count}'] = stat_col
                count += 1
        return self.parsed_stats


    def convert(self):
        for athlete, stat_col in self.parsed_stats.items():
            convert = modules.converter.Converter(stat_col)
            convert.convert()
            convert.merge()

            # for stat in stat_col:
            #     print(stat.__str__())


if __name__ == '__main__':
    void = VOID()   
    void.get_tables()
    void.stat_parse()
    void.convert()