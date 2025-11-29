from src.modules.math.factorial import factorial, factorial_recursive

# factorial tests


def test_factorial_negative():
    assert factorial(-1) == 0
    assert factorial(-5) == 0


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_two():
    assert factorial(2) == 2


def test_factorial_small_numbers():
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720


def test_factorial_medium_numbers():
    assert factorial(7) == 5040
    assert factorial(8) == 40320
    assert factorial(10) == 3628800


def test_factorial_large_numbers():
    assert factorial(20) == 2432902008176640000
    assert factorial(100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000


# recursive factorial tests
def test_factorial_recursive_negative():
    assert factorial_recursive(-1) == 0
    assert factorial_recursive(-5) == 0


def test_factorial_recursive_zero():
    assert factorial_recursive(0) == 1


def test_factorial_recursive_one():
    assert factorial_recursive(1) == 1


def test_factorial_recursive_two():
    assert factorial_recursive(2) == 2


def test_factorial_recursive_small_numbers():
    assert factorial_recursive(3) == 6
    assert factorial_recursive(4) == 24
    assert factorial_recursive(5) == 120
    assert factorial_recursive(6) == 720
