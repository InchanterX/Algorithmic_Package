from src.modules.sorts.bubble_sort import bubble_sort
from src.modules.sorts.bucket_sort import bucket_sort
from src.modules.sorts.counting_sort import counting_sort
from src.modules.sorts.heap_sort import heap_sort
from src.modules.sorts.quick_sort import quick_sort
from src.modules.sorts.radix_sort import radix_sort


def test_bubble_sort():
    # integers
    assert bubble_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert bubble_sort([5, -1, 3, 0]) == [-1, 0, 3, 5]

    # float numbers
    assert bubble_sort([3.5, 1.2, 4.8, 2.1]) == [1.2, 2.1, 3.5, 4.8]

    # strings
    assert bubble_sort(['c', 'a', 'b']) == ['a', 'b', 'c']


def test_bucket_sort():
    # float numbers
    assert bucket_sort([0.3, 0.1, 0.4, 0.2]) == [0.1, 0.2, 0.3, 0.4]
    assert bucket_sort([0.8, 0.5, 0.9, 0.1]) == [0.1, 0.5, 0.8, 0.9]


def test_counting_sort():
    # Positive integers
    assert counting_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert counting_sort([5, 2, 3, 1, 4]) == [1, 2, 3, 4, 5]


def test_heap_sort():
    # Integers
    assert heap_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert heap_sort([5, -1, 3, 0]) == [-1, 0, 3, 5]

    # Float
    assert heap_sort([3.5, 1.2, 4.8, 2.1]) == [1.2, 2.1, 3.5, 4.8]

    # Strings
    assert heap_sort(['c', 'a', 'b']) == ['a', 'b', 'c']


def test_quick_sort():
    # Integers
    assert quick_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert quick_sort([5, -1, 3, 0]) == [-1, 0, 3, 5]

    # Float
    assert quick_sort([3.5, 1.2, 4.8, 2.1]) == [1.2, 2.1, 3.5, 4.8]

    # Strings
    assert quick_sort(['c', 'a', 'b']) == ['a', 'b', 'c']


def test_radix_sort():
    # Positive integers
    assert radix_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert radix_sort([100, 25, 7, 333]) == [7, 25, 100, 333]


def test_empty_and_single():
    # tests for base cases

    # Empty arrays
    assert bubble_sort([]) == []
    assert bucket_sort([]) == []
    assert counting_sort([]) == []
    assert heap_sort([]) == []
    assert quick_sort([]) == []
    assert radix_sort([]) == []

    # Arrays with only one element
    assert bubble_sort([5]) == [5]
    assert bucket_sort([0.5]) == [0.5]
    assert counting_sort([3]) == [3]
    assert heap_sort([2]) == [2]
    assert quick_sort([1]) == [1]
    assert radix_sort([7]) == [7]
