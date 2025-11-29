from src.infrastructure.logger import logger


class Handler:
    def __init__(self):
        self._logger = logger

    def _convert_to_int(self, parameters: list) -> list[int]:
        for i in range(len(parameters)):
            try:
                parameters[i] = int(parameters[i])
            except ValueError:
                self._logger.exception(
                    f"Incorrect parameter {parameters[i]} was given.")
                raise ValueError(
                    f"Incorrect parameter {parameters[i]} was given!")
        return parameters

    def _convert_to_float_and_int(self, parameters: list) -> list[int]:
        for i in range(len(parameters)):
            try:
                if ',' in parameters[i] or '.' in parameters[i]:
                    parameters[i] = float(parameters[i])
                else:
                    parameters[i] = int(parameters[i])
            except ValueError:
                self._logger.exception(
                    f"Incorrect parameter {parameters[i]} was given.")
                raise ValueError(
                    f"Incorrect parameter {parameters[i]} was given!")
        return parameters

    def handler(self, command: str, parameters: list) -> list | int:
        if command in ["fibonacci", "factorial"]:
            if len(parameters) == 1:
                int_parameters = self._convert_to_int(parameters)
                self._logger.debug(
                    "Successfully converted parameters to 'int'.")
                return int_parameters[0]
            else:
                self._logger.exception("Incorrect parameters quantity.")
                raise SyntaxError("Incorrect parameters quantity.")
        elif command in ["bubble-sort", "quick-sort", "heap-sort"]:
            return parameters
        elif command in ["bucket-sort", "counting-sort", "radix-sort"]:
            converted_parameters = self._convert_to_float_and_int(parameters)
            self._logger.debug(
                "Successfully converted parameters to float/int.")
            return converted_parameters
        else:
            self._logger.exception("This isn't possible!")
            raise SyntaxError("This isn't possible!")
