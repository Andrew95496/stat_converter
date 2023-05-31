import modules
import configs

import os

# load_dir = config['DEFAULTS']['LOAD_DIR']
# athletes = ast.literal_eval(config['DEFAULTS']['ATHLETES'])
# sheet_name = config['DEFAULTS']['SHEET_NAME']


# athlete: str | None = None, opponent: str | None = None, time: list[str] = None
class VOID():

    def __init__(self, tables: list[dict] | None = None, parsed_stats: list[dict] | None = None) -> None:
        if tables is None:
            self.tables = {}
        if parsed_stats is None:
            self.parsed_stats = {}
        # self.athlete = athlete
        # self.opponent = opponent
        # self.time = time
        os.system('bash saves.sh')



    def get_tables(self):
        for athlete in configs.ATHLETES:
            dataframe = modules.FileImporter(
                athlete, f'{athlete}{configs.SHEET_NAME}', f'{configs.LOAD_DIR}{athlete}.xlsx')
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
            convert._change_suffix()
            convert._change_direction()
            convert._change_postion()
            # for stat in stat_col:
            #     print(stat.__str__())



if __name__ == '__main__':
    void = VOID()   
    void.get_tables()
    void.stat_parse()
    void.convert()