It's a Algorithmic Package - project with implementations of 6 different sorting algorithms, stack, queue and several math functions.

# Project structure

 <pre>
    .
    ├── Algorithmic_Package
    │   ├── .algorithms_log/                   # project logs
    │   ├── src/                               # Source code
    │       ├── common/                        # main functions of the console
    │            ├── __init__.py               #
    │            ├── config.py                 # logging config
    │       ├── infrastructure/                # main functions of the console
    │            ├── __init__.py               #
    │            ├── constants.py              # just constants
    │            ├── handler.py                # check commands parameters
    │            ├── logger.py                 # logging module
    │            ├── validator.py              # process given commands
    │       ├── modules/                       # all project modules
    │            ├── addons/                   #
    │                 ├── __init__.py          #
    │                 ├── array_generator.py   #
    │            ├── datatypes/                # datatypes
    │                 ├── __init__.py          #
    │                 ├── queue.py             # queue data type
    │                 ├── stack.py             # stack data type
    │            ├── math/                     # math functions
    │                 ├── __init__.py          #
    │                 ├── factorial.py         # factorial functions
    │                 ├── fibonacci.py         # fibonacci functions
    │            ├── sorts/                    #
    │                 ├── __init__.py          #
    │                 ├── __init__.py          #
    │                 ├── __init__.py          #
    │       ├── package/                       # project building folder
    │            ├── __init__.py               #
    │            ├── package.py                # gather all classes in one for a simpler usage
    |       ├── __init__.py                    #
    |       ├── main.py                        # It's a main file!
    │   ├── tests/                             # Unit tests
    │   ├── .gitignore                         # git ignore files
    │   ├── .pre-commit-config.yaml            # Code-style check
    │   ├── pyproject.toml                     # Project configuration
    │   ├── README.md                          # Laboratory report with a project description
</pre>

# Set up
To use this package you need to download it. Then you can run it from the project root with your terminal with:
```
python -m src.main
```

## Tests
To run tests you need to have pytest, pytest-cov.
To activate tests use:
```
python -m pytest
```

# How it works
## Constants
Constants of program: regular expressions, paths, modules dictionary

## Main
Main file where CLI starts, supports exiting with ctrl + c or exit/quit

## Package
File where all the infrastructure gather

## Logger
Logger module that used across the project

## Validator
Split the command written by user by spaces and tabs, exclude all dump cases that can break the program

## Handler
Process commands parameters to move all the checks out of algorithms

# Algorithms Package is self
Package is split into submodules
## Data types
Contain queue that works on the principe of FILO (First In Last Out) therefor first put element will be removed first from it. And stack that works on the principe of FIFO (First In First Out) therefor last put element will be removed first. Types supports functions:
__init__, is_empty, __len__ for both
enqueue, dequeue, front for queue
and push, pop, peek, min for stack.
Function min works with complexity of O(1) owing to storing last min element in last element.

## Math
### Fibonacci
Contains two function: optimized and not optimized. Not optimized works on recursions. Optimized count number using mathematical Bine formula.

### Factorial
Contains two function: optimized and not optimized. Not optimized works on recursions. Optimized use Eratosthenes's sieve and get result by multiplying powers of number decomposition by primes.

## Sorts
### bubble_sort
Bubble sort algorithm sort array by raising up greater elements up inside the array while it won't be sorted

### bucket_sort
Bucket sort split given elements to the buckets with index that is closest to the element ratio to buckets amount. Then sort buckets using insertion_sort and unite it to the result.

### counting_sort
Sorting algorithm that efficient on small range of numbers. Algorithms count appearances of elements and sort them

### heap_sort
Algorithm build "heap" from given data Extract elements from the heap and place max element to the end. Than gather everything one by one to get a result.

### quick_sort
Really quick sort. It is even cold quick sort.
Split array into two parts. Smaller to left, greater to right and make a recursive call of new parts.

### radix_sort
Version (in my case) of the radix algorithms that works on buckets. It stores digits in 10 buckets for every digit and sort numbers by the units, tens and on.
