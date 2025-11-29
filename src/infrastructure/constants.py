import re
import os
from src.modules.math.fibonacci import fibonacci, fibonacci_recursive
from src.modules.math.factorial import factorial, factorial_recursive

LOG_DIR = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "../../.algorithms_log")

FUNCTIONS = {
    "fibonacci": fibonacci,
    "fibonacci-recursive": fibonacci_recursive,
    "factorial": factorial,
    "factorial_recursive": factorial_recursive,
}

TOKEN_RE = r"[a-zA-Z]+(?:-[a-zA-Z]+)*|-?\d+"
REGULAR_EXPRESSION = re.compile(TOKEN_RE)
# PARAMETERS_RE = r"[^\s]+"
# REGULAR_EXPRESSION = re.compile("|".join([COMMAND_RE, PARAMETERS_RE]))
