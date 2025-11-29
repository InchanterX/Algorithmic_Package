import src.infrastructure.constants as constants
from src.infrastructure.logger import logger
import re


class Validator:
    def __init__(self):
        self._logger = logger

    def _tokenize(self, command: str) -> list:
        return re.findall(constants.REGULAR_EXPRESSION, command)

    def validator(self, user_command: str) -> list[str, list[str]]:

        # splitting users input to tokens
        tokens = self._tokenize(user_command)
        self._logger.debug(f"Tokenized line {user_command}.")

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
