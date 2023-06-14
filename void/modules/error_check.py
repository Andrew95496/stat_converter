from statics import COMPLETED_STATS
from Errors.error_types import ErrorTypes
from stat_object import Stat

# TODO BUG: (L)GPa <- (R)GP would be valid [NOT CORRECT] 
class ErrorCheck():

    __slots__ = ('stats')

    #  Checks if attempts come before a completed action
    def attempt_previous(self, stats: list[str]) -> None:
        prev_stat = 'Start'
        for stat in stats:
            rd_stat = Stat.remove_direction(stat)
            print(prev_stat, '<-', stat)
            if rd_stat in COMPLETED_STATS and (prev_stat == 'Start' or prev_stat.endswith('a') == False):
                ErrorTypes.no_attempt_error(stat)
            prev_stat = stat
                
            