from .statics import ALL_STATS, NO_DIRECTION, TYPES
from .stat_object import Stat
from .Errors.error_types import ErrorTypes

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
    def __assign__types(stat: str) -> str:
        for base_stat in ALL_STATS['Base Stats']:
            if base_stat in stat:
                stat = base_stat
        
        for key, types_list in TYPES.items():
            for stat_ in types_list:
                if stat_ == stat:
                    return key

        

    @staticmethod
    def __assign_direction(stat: str) -> str | None:
        return stat[1] if stat not in NO_DIRECTION else None

    @staticmethod
    def __assign_position(stat: str) -> str | None:
        for position_stat in ALL_STATS['Position Types']:
            if position_stat in stat:
                return position_stat
        return None

    @staticmethod
    def __assign_prefix(stat: str) -> str | None:
        for prefix in ALL_STATS['Execution Prefix']:
            if prefix in stat:
                return prefix
        return None
        

    @staticmethod
    def __assign__stat(stat: str) -> str:
        for base_stat in ALL_STATS['Base Stats']:
            if base_stat in stat:
                return base_stat
        ErrorTypes.ERROR(stat, 11) # Stat was not matched
        return 'NOT VALID'

    @staticmethod
    # TODO: Adds 'a' to suffix_list with stats ending only in 'ag' ex: (L)GpLEEag -> suffix_list = ['a', 'ag'] NEEDS FIX
    def __assign__suffix(stat: str):
        suffix_list: list = []
        for suffix in ALL_STATS['Execution Suffix']:
            if suffix in stat:
                suffix_list.append(f'{suffix}O:=')
        return suffix_list



    @staticmethod
    def __is_completed(stat: str) -> bool:
        return True if stat.endswith('a') else False
            


    def assign_type(self, stat_list) -> Stat:
        stat_obj_list = []
        prev_stat = None
        for _stat in stat_list:
            full_stat = _stat
            type = StatType.__assign__types(_stat)
            direction = StatType.__assign_direction(_stat)
            position = StatType.__assign_position(_stat)
            prefixes = StatType.__assign_prefix(_stat)
            stat = StatType.__assign__stat(_stat)
            suffixes = StatType.__assign__suffix(_stat)
            is_attempt = StatType.__is_completed(_stat)

            __stat__ = Stat(prev_stat, full_stat, type, direction, position, prefixes, stat, suffixes, is_attempt)
            print(__stat__.__str__())
            stat_obj_list.append(__stat__)
            prev_stat = _stat
        return stat_obj_list
    
        

    
            
