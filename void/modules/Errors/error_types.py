from ..color_code import bcolors as bc

class ErrorTypes():

    @staticmethod
    def ERROR(stat: str, case: str) -> None:
        match case:
            case 10:
                print(f'{bc.FAIL}{stat}: NEEDS PREVIOUS ATTEMPT{bc.ENDC}')
                return f'{stat}: NEEDS PREVIOUS ATTEMPT'
            case 11:
                print(f'{bc.FAIL}{stat}: INVALID{bc.ENDC}')
                return f'{stat}: INVALID'

    @staticmethod
    def WARNING(stat: str, case: str) -> None:
        match case:
            case 20:
                print(f'{bc.WARNING}CHECK {bc.BOLD}{stat}{bc.ENDC}'f'{bc.WARNING} DIRECTION CHANGE, RESULTS MAY NOT BE ACCURATE{bc.ENDC}')
                return f'CHECK {stat} DIRECTION CHANGE, RESULTS MAY NOT BE ACCURATE'

