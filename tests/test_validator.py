import pytest
from src.infrastructure.handler import Handler


def test_convert_to_int_valid():
    handler = Handler()
    params = ["1", "2", "3"]
    result = handler._convert_to_int(params)
    assert result == [1, 2, 3]
    assert all(isinstance(x, int) for x in result)


def test_convert_to_int_invalid():
    handler = Handler()
    params = ["1", "abc", "3"]
    with pytest.raises(ValueError, match="Incorrect parameter abc was given!"):
        handler._convert_to_int(params)


def test_convert_to_int_mixed_invalid():
    handler = Handler()
    params = ["1.5", "2"]
    with pytest.raises(ValueError, match="Incorrect parameter 1.5 was given!"):
        handler._convert_to_int(params)


def test_convert_to_float_and_int_integers():
    handler = Handler()
    params = ["1", "2", "3"]
    result = handler._convert_to_float_and_int(params)
    assert result == [1, 2, 3]
    assert all(isinstance(x, int) for x in result)


def test_convert_to_float_and_int_floats():
    handler = Handler()
    params = ["1.5", "2.7", "3.0"]
    result = handler._convert_to_float_and_int(params)
    assert result == [1.5, 2.7, 3.0]
    assert all(isinstance(x, float) for x in result)


def test_convert_to_float_and_int_mixed():
    handler = Handler()
    params = ["1", "2.5", "3"]
    result = handler._convert_to_float_and_int(params)
    assert result == [1, 2.5, 3]
    assert isinstance(result[0], int)
    assert isinstance(result[1], float)
    assert isinstance(result[2], int)


def test_convert_to_float_and_int_with_comma():
    handler = Handler()
    params = ["1,5", "2,7"]
    result = handler._convert_to_float_and_int(params)
    assert result == [1.5, 2.7]
    assert all(isinstance(x, float) for x in result)


def test_convert_to_float_and_int_invalid():
    handler = Handler()
    params = ["1", "abc", "3.5"]
    with pytest.raises(ValueError, match="Incorrect parameter abc was given!"):
        handler._convert_to_float_and_int(params)


def test_handler_fibonacci_valid():
    handler = Handler()
    result = handler.handler("fibonacci", ["5"])
    assert result == 5
    assert isinstance(result, int)


def test_handler_factorial_valid():
    handler = Handler()
    result = handler.handler("factorial", ["3"])
    assert result == 3
    assert isinstance(result, int)


def test_handler_fibonacci_invalid_quantity():
    handler = Handler()
    with pytest.raises(SyntaxError, match="Incorrect parameters quantity."):
        handler.handler("fibonacci", ["5", "3"])


def test_handler_factorial_invalid_quantity():
    handler = Handler()
    with pytest.raises(SyntaxError, match="Incorrect parameters quantity."):
        handler.handler("factorial", [])


def test_handler_fibonacci_invalid_parameter():
    handler = Handler()
    with pytest.raises(ValueError, match="Incorrect parameter abc was given!"):
        handler.handler("fibonacci", ["abc"])


def test_handler_bubble_sort():
    handler = Handler()
    params = ["3", "1", "2"]
    result = handler.handler("bubble-sort", params)
    assert result == ["3", "1", "2"]
    assert all(isinstance(x, str) for x in result)


def test_handler_quick_sort():
    handler = Handler()
    params = ["5", "4", "3"]
    result = handler.handler("quick-sort", params)
    assert result == ["5", "4", "3"]


def test_handler_heap_sort():
    handler = Handler()
    params = ["a", "b", "c"]
    result = handler.handler("heap-sort", params)
    assert result == ["a", "b", "c"]


def test_handler_bucket_sort_integers():
    handler = Handler()
    params = ["1", "2", "3"]
    result = handler.handler("bucket-sort", params)
    assert result == [1, 2, 3]
    assert all(isinstance(x, int) for x in result)


def test_handler_bucket_sort_floats():
    handler = Handler()
    params = ["1.5", "2.7", "3.0"]
    result = handler.handler("bucket-sort", params)
    assert result == [1.5, 2.7, 3.0]
    assert all(isinstance(x, float) for x in result)


def test_handler_counting_sort():
    handler = Handler()
    params = ["5", "3", "1"]
    result = handler.handler("counting-sort", params)
    assert result == [5, 3, 1]
    assert all(isinstance(x, int) for x in result)


def test_handler_radix_sort():
    handler = Handler()
    params = ["100", "50", "25"]
    result = handler.handler("radix-sort", params)
    assert result == [100, 50, 25]
    assert all(isinstance(x, int) for x in result)


def test_handler_bucket_sort_mixed():
    handler = Handler()
    params = ["1", "2.5", "3"]
    result = handler.handler("bucket-sort", params)
    assert result == [1, 2.5, 3]
    assert isinstance(result[0], int)
    assert isinstance(result[1], float)
    assert isinstance(result[2], int)


def test_handler_bucket_sort_invalid():
    handler = Handler()
    with pytest.raises(ValueError, match="Incorrect parameter abc was given!"):
        handler.handler("bucket-sort", ["1", "abc", "3"])


def test_handler_unknown_command():
    handler = Handler()
    with pytest.raises(SyntaxError, match="This isn't possible!"):
        handler.handler("unknown-command", ["1", "2"])


def test_handler_empty_command():
    handler = Handler()
    with pytest.raises(SyntaxError, match="This isn't possible!"):
        handler.handler("", ["1"])
