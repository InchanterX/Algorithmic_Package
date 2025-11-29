import re
import os
from src.modules.math.fibonacci import fibonacci, fibonacci_recursive
from src.modules.math.factorial import factorial, factorial_recursive
from src.modules.sorts.bubble_sort import bubble_sort
from src.modules.sorts.bucket_sort import bucket_sort
from src.modules.sorts.counting_sort import counting_sort
from src.modules.sorts.heap_sort import heap_sort
from src.modules.sorts.quick_sort import quick_sort
from src.modules.sorts.radix_sort import radix_sort


# logging directory
LOG_DIR = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "../../.algorithms_log")

# all modules's elements
FUNCTIONS = {
    "fibonacci": fibonacci,
    "fibonacci-recursive": fibonacci_recursive,
    "factorial": factorial,
    "factorial-recursive": factorial_recursive,
    "bubble-sort": bubble_sort,
    "bucket-sort": bucket_sort,
    "counting-sort": counting_sort,
    "heap-sort": heap_sort,
    "quick-sort": quick_sort,
    "radix-sort": radix_sort,
}

# regular expression for user's input
TOKEN_RE = r"[a-zA-Z]+(?:[-.][a-zA-Z]+)*|-?\d*\.?\d+"
REGULAR_EXPRESSION = re.compile(TOKEN_RE)
