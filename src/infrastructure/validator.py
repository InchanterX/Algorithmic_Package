import src.infrastructure.constants as constants
from src.infrastructure.logger import logger
import re


class Validator:
    '''
    Tokenize and process inputted command
    Raise a error if given command does not exist or not given
    Return command and list of parameters separately
    '''

    def __init__(self):
        self._logger = logger

    def _tokenize(self, command: str) -> list:
        '''
        Tokenize given line dividing it by separating symbols
        Return list of tokens
        '''
        return re.findall(constants.REGULAR_EXPRESSION, command)

    def validator(self, user_command: str) -> list:
        '''
        Validate given command by splitting it to tokens, check for mistakes and return the list of tokens
        Raise an exception if given command is empty or if command not in a list of commands
        '''

        # splitting users input to tokens
        tokens = self._tokenize(user_command)
        self._logger.debug(f"Tokenized line {user_command}.")

        # empty string was given
        if not tokens:
            self._logger.exception("Input is empty.")
            raise SyntaxError("Input is empty!")

        # command validation
        command = tokens[0]
        if command not in constants.FUNCTIONS.keys():
            self._logger.exception(
                f"{command} is invalid therefore can be executed.")
            raise SyntaxError(f"{command} is not a module's command!")

        # preparing parameters
        arguments = tokens[1:]
        return [command, arguments]
