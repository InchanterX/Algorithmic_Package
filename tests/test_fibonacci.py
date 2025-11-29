from src.modules.math.fibonacci import fibonacci, fibonacci_recursive

# fibonacci tests


def test_fibonacci_small_numbers():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8


def test_fibonacci_medium_numbers():
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55


def test_fibonacci_larger_numbers():
    assert fibonacci(15) == 610
    assert fibonacci(20) == 6765

# recursive fibonacci tests


def test_fibonacci_recursive_small_numbers():
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(3) == 2
    assert fibonacci_recursive(4) == 3
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(6) == 8


def test_fibonacci_recursive_medium_numbers():
    assert fibonacci_recursive(7) == 13
    assert fibonacci_recursive(8) == 21
    assert fibonacci_recursive(9) == 34
    assert fibonacci_recursive(10) == 55
