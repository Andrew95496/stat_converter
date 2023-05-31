# MODULES
from .statics import CHANGE_DIRECTION, DIRECTION_WARNING, ALL_STATS
from .Errors.error_types import ErrorTypes


# @property
class Converter():    

    def __init__(self, stat_obj_list, new_stats=None):
        self.stat_obj_list = stat_obj_list
        if new_stats is None:
         self.new_stats = []
    

    # TODO: Get converter to wok with Stat Object
    #Adds an ag(against) or removes ag for all appropriate stats
    def _change_suffix(self) -> None:
        for stat_obj in self.stat_obj_list:
            if 'ag' in stat_obj.suffixes:
                stat_obj.suffixes.remove('ag')
            if stat_obj.stat in ALL_STATS['Base Stats'] and stat_obj.stat != 'Scr':
                stat_obj.suffixes.append('agC:=')


    #Changes the direction of stats
        # ex: (L)GPa -> (R)GPaag
    def _change_direction(self) -> None:
        for stat_obj in self.stat_obj_list:
            if stat_obj.direction:
                if stat_obj.stat in CHANGE_DIRECTION:
                    case = stat_obj.direction
                    match case:
                        case 'L':
                            stat_obj.direction = 'R'
                        case 'R':
                            stat_obj.direction = 'L'
            
            if stat_obj.stat in DIRECTION_WARNING:
                ErrorTypes.WARNING(stat_obj.full_stat, 20)


    def _change_postion(self):
        for stat_obj in self.stat_obj_list:
            case =  stat_obj.position
            match case:
                case 'Gp':
                    stat_obj.position = 'G'
                case 'G':
                    stat_obj.position = 'Gp'


    def convert(self):
        pass
    





    