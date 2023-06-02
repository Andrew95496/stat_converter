from .color_code import bcolors as bc


class Stat():

    def __init__(self, prev_stat: str | bool, full_stat, type: str, direction: str | bool, position: str | bool, prefixes: str, stat: str, suffixes: list, is_attempt, flags = None) -> str:
        self.prev_stat = prev_stat
        self.full_stat = full_stat
        self.type = type
        self.direction = direction
        self.position = position
        self.prefixes = prefixes
        self.stat = stat
        self.suffixes = suffixes
        self.is_attempt = is_attempt
        print(f'{bc.BOLD}{bc.OKGREEN}{self.full_stat} initialized{bc.ENDC}')

    def __str__(self) -> str:
        return f'''{bc.HEADER}
        Previous: {self.prev_stat}\n
        Full: {self.full_stat}\n
        Type: {self.type}\n
        Direction: {self.direction}\n
        Position: {self.position}\n
        Prefixes: {self.prefixes}\n
        Stat: {self.stat}\n
        Suffix: {self.suffixes}\n
        Attempt: {self.is_attempt}\n
        {bc.ENDC}
        '''

