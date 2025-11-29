from src.infrastructure.logger import logger
import logging.config
from src.common.config import LOGGING_CONFIG
import src.infrastructure.constants as constants
from src.infrastructure.validator import Validator


def main() -> None:
    # define logger in accordance with config file
    logging.config.dictConfig(LOGGING_CONFIG)
    logger.info("Logging initialized.")
    print("Algorithmic package CLI is loading...")

    try:
        while True:
            # read user command
            command = input("> ")
            logger.info(f"User entered command: {command}")

            # stop the program if stop word was given
            if command.lower() in ("exit", "quit"):
                print("Exiting the CLI.")
                logger.info("Logging stopped.")
                break

            # parsing inputted command
            validator = Validator()
            parsed_command, parameters = validator.validator(command)

            # applying function according to the function name
            function = constants.FUNCTIONS[parsed_command]
            result = function(int(parameters[0]))
            print(">", result)

    except KeyboardInterrupt:
        print("Exiting the console.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
