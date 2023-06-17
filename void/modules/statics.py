ALL_STATS: dict = {'Position Types': {'Td', 'Gp', 'Gu', 'Pos'},
             'Execution Prefix': {'cl', 'n', 'ct', '+', '-', '='},
             'Base Stats': {'GTD', 'FSW', 'SLTD', 'DLTD', 'Th', 'CTD', 'SCT', 'GUP', 'Sd',
                            'GP', 'OB', 'Sw', 'LEE', 'PA', 'PT', 'PE', 'PL', 'Pin', 'Sub',
                            'Pen', 'Warning', 'Rv', 'AlSu', 'fSu', 'Scr', 'Bt'},
             'Execution Suffix': {'ch', 'a', 'ag'}}

TYPES: dict = {'Takedown': ['GTD', 'FSW', 'SLTD', 'DLTD', 'Th', 'CTD'],
         'Standing': ['SCT', 'GUP', 'Sd'],
         'Guard Pass': ['GP'],
         'Guard': ['OB', 'Sw'],
         'Leg Entanglement': ['LEE'],
         'Position': ['PA', 'PT', 'PE', 'PL', 'Pin'],
         'Submission': ['Sub'],
         'Penalty/Warning': ['Pen', 'Warning'],
         'Reversal': ['Rv'],
         'Stand-ups': ['AlSu', 'fSu'],
         'Scramble': ['Scr'],
         'Back Take': ['Bt']
         }




# STATS WITH NO (L), (M), (R)
# TODO: ADD Positions and prefixes to applicable Stats
NO_DIRECTION: set = {'PA', 'PT', 'PE', 'PL', 'Pin', 'Pen', 'AlSu',
                'fSu', 'Scr', 'Bt', 'SCT', 'P', 'Warning'}  # P is Depreciated

CHANGE_DIRECTION: set = {'DLTD', 'SLTD', 'GP', 'OB', 'Sw'}

DIRECTION_WARNING: set = {'FSW', 'Sw', 'OB', 'CTD', 'Th'}

# Stats that do not have an easy opposite statistic
# ex: PL -> cPE or PR vise versa
# ex: +Scr -> -Scr
SPECIAL_STATS = {'Scr'}


# Some stats are linked with other stats
# ex: Bt [PA, PT]
LINKED_STATS: dict = {'Bt': 'PT | PA', 'PT': 'PA warning: may not always be applicable see DOCS', 'PA': 'PT'}
