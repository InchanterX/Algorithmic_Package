import pytest
from src.modules.datatypes.queue import Queue


def test_enqueue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


def test_front():
    queue = Queue()
    queue.enqueue(5)
    assert queue.front() == 5
    assert len(queue) == 1


def test_is_empty():
    queue = Queue()
    assert queue.is_empty()
    queue.enqueue(1)
    assert not queue.is_empty()
    queue.dequeue()
    assert queue.is_empty()


def test_len():
    queue = Queue()
    assert len(queue) == 0
    queue.enqueue(1)
    queue.enqueue(2)
    assert len(queue) == 2
    queue.dequeue()
    assert len(queue) == 1


def test_dequeue_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()


def test_front_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.front()
