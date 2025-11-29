from src.infrastructure.logger import logger


class Queue:
    def __init__(self):
        '''Initialize queue'''
        self._logger = logger
        self._queue = []

    def enqueue(self, element: int) -> None:
        '''Add element to queue'''
        self._queue.append(element)

    def is_empty(self) -> bool:
        '''Check queue for being empty'''
        if len(self._queue) == 0:
            return True
        else:
            return False

    def dequeue(self) -> int:
        '''Pop the first element from the queue'''
        if self.is_empty():
            self._logger.exception(
                "Can't delete element from empty queue.")
            raise IndexError("Can't delete element from empty queue!")
        return self._queue.pop(0)

    def front(self) -> int:
        '''Return first queue element'''
        if self.is_empty():
            self._logger.exception(
                "Can't show element from empty queue.")
            raise IndexError("Can't show element from empty queue!")
        return self._queue[0]

    def __len__(self):
        '''Returns len of the queue'''
        return len(self._queue)
