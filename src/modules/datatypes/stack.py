from src.infrastructure.logger import logger


class Stack:
    def __init__(self):
        '''Stack initialization'''
        self._logger = logger
        self._stack = []

    def push(self, element: int) -> None:
        '''Add element to stack'''
        # find min element
        if self.is_empty():
            min_value = element
        else:
            min_value = min(element, self._stack[-1][1])

        self._stack.append((element, min_value))

    def is_empty(self) -> bool:
        '''Check stack for being empty'''
        if len(self._stack) == 0:
            return True
        else:
            return False

    def pop(self) -> int:
        '''Pop element from the stack top'''
        if self.is_empty():
            self._logger.exception(
                "Can't pop element from the empty stack.")
            raise IndexError("Can't pop element from the empty stack!")

        value, element = self._stack.pop()
        return value

    def peek(self) -> int:
        '''Return top element'''
        if self.is_empty():
            self._logger.exception(
                "Can't peek element from the empty stack.")
            raise IndexError("Can't peek element from the empty stack!")
        return self._stack[-1][0]

    def __len__(self) -> int:
        return len(self._stack)

    def min(self) -> int:
        '''Returns minimal element in O(1) complexity'''
        if self.is_empty():
            self._logger.exception(
                "There is no min element in empty stack.")
            raise ValueError("There is no min element in empty stack!")
        return self._stack[-1][1]
