from .statics import ALL_STATS, NO_DIRECTION, TYPES
from .stat_object import Stat
from .Errors.error_types import ErrorTypes
from .stat_logger import StatLogger

# '(R)SLTda',
# '(R)FSwa',
# '(R)FSwa',
# '(L)Tha',
# '(R)Tha',
# '(R)Cag',
# 'PosfSua',
# 'PRa',
# 'PR',
# '(R)GPLEEa',
# '(R)GPLEE',
# '(R)GPSuba',
# '(R)GPSub'



class StatType():


    @staticmethod
    def __type__(stat: str) -> str:
        for base_stat in ALL_STATS['Base Stats']:
            if base_stat in stat:
                stat = base_stat # Find the base_stat that matches the stat param (L)GPa = GP  stat = GP
                
        for key, types_list in TYPES.items(): # SEE statics.py
            for stat_ in types_list:
                if stat_ == stat: 
                    return key

        

    @staticmethod
    def __direction__(stat: str) -> str:
        print(stat)
        return stat[1] if stat not in NO_DIRECTION and stat[1] in ('L', 'M', 'R') else ''

    @staticmethod
    def __position__(stat: str) -> str:
        for position_stat in ALL_STATS['Position Types']:
            if position_stat in stat:
                return position_stat
        return ''

    @staticmethod
    def __prefix__(stat: str) -> str:
        for prefix in ALL_STATS['Execution Prefix']:
            if prefix in stat:
                return prefix
        return ''
        

    @staticmethod
    def __stat__(stat: str) -> str:
        for base_stat in ALL_STATS['Base Stats']:
            if base_stat in stat:
                return base_stat
        x = ErrorTypes.ERROR(stat, 11)
        StatLogger(x)
         # Stat was not matched
        return 'NOT VALID'

    @staticmethod
    # TODO: Adds 'a' to suffix_list with stats ending only in 'ag' ex: (L)GpLEEag -> suffix_list = ['a', 'ag'] NEEDS FIX
    def __suffix__(stat: str):
        suffix_list: list = []
        for suffix in ALL_STATS['Execution Suffix']:
            if suffix in stat:
                suffix_list.append(suffix)
        return suffix_list



    @staticmethod
    def __completed__(stat: str) -> bool:
        return True if stat.endswith('a') else False
            


    def assign_type(self, stat_list) -> Stat:
        stat_obj_list = []
        prev_stat = None
        for _stat in stat_list:
            full_stat = _stat
            type = StatType.__type__(_stat)
            direction = StatType.__direction__(_stat)
            position = StatType.__position__(_stat)
            prefixes = StatType.__prefix__(_stat)
            stat = StatType.__stat__(_stat)
            suffixes = StatType.__suffix__(_stat)
            is_attempt = StatType.__completed__(_stat)

            if _stat not in NO_DIRECTION and direction == '':
                print(f'ERROR: YOU DID SOMETHING WRONG {_stat}')


            __stat__ = Stat(prev_stat, full_stat, type, direction, position, prefixes, stat, suffixes, is_attempt)
            # print(__stat__.__str__())
            stat_obj_list.append(__stat__)
            prev_stat = _stat
        return stat_obj_list
    
        

    
            
