import re
import os
from src.modules.math.fibonacci import fibonacci, fibonacci_recursive
from src.modules.math.factorial import factorial, factorial_recursive

# logging directory
LOG_DIR = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "../../.algorithms_log")

# all modules's elements
FUNCTIONS = {
    "fibonacci": fibonacci,
    "fibonacci-recursive": fibonacci_recursive,
    "factorial": factorial,
    "factorial_recursive": factorial_recursive,
}

# regular expression for user's input
TOKEN_RE = r"[a-zA-Z]+(?:-[a-zA-Z]+)*|-?\d+"
REGULAR_EXPRESSION = re.compile(TOKEN_RE)
