import modules
import configs

import os

# load_dir = config['DEFAULTS']['LOAD_DIR']
# athletes = ast.literal_eval(config['DEFAULTS']['ATHLETES'])
# sheet_name = config['DEFAULTS']['SHEET_NAME']


# athlete: str | None = None, opponent: str | None = None, time: list[str] = None
class VOID():

    def __init__(self, dataframe = None, import_dir=configs.Config.IMPORT_DIR, sheet_name=configs.Config.SHEET_NAME, athletes: list[str] = configs.Config.ATHLETES, tables: list[dict] | None = None, parsed_stats: list[dict] | None = None) -> None:
        self.dataframe = dataframe
        self.import_dir = import_dir
        self.sheet_name = sheet_name
        self.athletes = athletes
        if tables is None:
            self.tables = {}
        if parsed_stats is None:
            self.parsed_stats = {}
        os.system('bash saves.sh')



    def get_tables(self):
        for athlete in self.athletes:
            dataframe = modules.FileImporter(athlete, f'{athlete}{self.sheet_name}', f'{self.import_dir}{athlete}.xlsx')
            dataframe = dataframe.import_excel()
            self.tables[athlete] = (dataframe)
        return self.tables
    
    def stat_parse(self,athlete, table):
        athlete = athlete.replace('_', ' ')
        stats = modules.stat_type.StatType()
        stat_col = stats.assign_type(table['Stats'])
        self.parsed_stats[athlete] = stat_col


    def convert(self, stat_col, table):
        convert = modules.converter.Converter(stat_col)
        convert.convert()
        new = convert.merge()

        try:
            table['Stats '] = new
            table.fillna("",inplace=True)
            print(table.iloc[0:, [2, 7, 0, 3, 4, 5, 6]])
        except ValueError:
            print('DID NOT WORK')



if __name__ == '__main__':
    void = VOID()   
    tables = void.get_tables()
    for athlete, dataframes in tables.items():
        for table in dataframes:
            void.stat_parse(athlete, table)
            for stat_col in void.parsed_stats.values():
                void.convert(stat_col, table)

