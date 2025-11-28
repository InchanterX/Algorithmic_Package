import re
import os
from src.modules.math.fibonacci import fibonacci, fibonacci_recursive
from src.modules.math.factorial import factorial, factorial_recursive

LOG_DIR = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "../../.algorithms_log")
print(LOG_DIR)

FUNCTIONS = {
    "fibonacci": fibonacci,
    "fibonacci-recursive": fibonacci_recursive,
    "factorial": factorial,
    "factorial_recursive": factorial_recursive,
}

COMMAND_RE = r"(a-zA-Z-)*"
PARAMETERS_RE = r"[\s]*"
REGULAR_EXPRESSION = re.compile("|".join([COMMAND_RE, PARAMETERS_RE]))
