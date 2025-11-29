import src.infrastructure.constants as constants
from src.infrastructure.validator import Validator
from src.infrastructure.handler import Handler
from typing import Any


class Package:
    '''
    A class with flow of program elements calls too use them with one call were it is needed.
    '''

    def __init__(self):
        pass

    def package(self, command) -> Any:
        # parsing inputted command
        validator = Validator()
        parsed_command, parameters = validator.validator(command)

        print(parsed_command, parameters)
        # checking given parameters
        handler = Handler()
        parameters = handler.handler(parsed_command, parameters)

        # applying function according to the function name
        function = constants.FUNCTIONS[parsed_command]
        result = function(parameters)
        return result
