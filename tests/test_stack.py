
import pytest
from src.modules.datatypes.stack import Stack


def test_push_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_peek():
    stack = Stack()
    stack.push(5)
    assert stack.peek() == 5
    assert len(stack) == 1


def test_is_empty():
    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()


def test_len():
    stack = Stack()
    assert len(stack) == 0
    stack.push(1)
    stack.push(2)
    assert len(stack) == 2
    stack.pop()
    assert len(stack) == 1


def test_min():
    stack = Stack()
    stack.push(3)
    assert stack.min() == 3
    stack.push(5)
    assert stack.min() == 3
    stack.push(2)
    assert stack.min() == 2
    stack.push(1)
    assert stack.min() == 1
    stack.pop()
    assert stack.min() == 2


def test_min_with_duplicates():
    stack = Stack()
    stack.push(2)
    stack.push(2)
    stack.push(1)
    stack.push(1)
    assert stack.min() == 1
    stack.pop()
    assert stack.min() == 1
    stack.pop()
    assert stack.min() == 2


def test_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()


def test_peek_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()


def test_min_empty():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.min()
