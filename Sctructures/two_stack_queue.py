from stack import Stack
from typing import Union, Any


class TwoStackGreedyQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.size = 0

    def enqueue(self, value: Any = None):
        self.s1.push(value)
        self.size += 1

    def dequeue(self) -> Union[Any, None]:
        self.size = max(self.size - 1, 0)
        while self.s1.size:
            self.s2.push(self.s1.pop())

        value = self.s2.pop()

        while self.s2.size:
            self.s1.push(self.s2.pop())

        return value


class TwoStackOptimizedQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.size = 0

    def enqueue(self, value: Any = None):
        self.s1.push(value)
        self.size += 1

    def dequeue(self) -> Union[Any, None]:
        if self.s2.size:
            self.size -= 1
            return self.s2.pop()

        while self.s1.size:
            self.s2.push(self.s1.pop())

        self.size -= 1
        return self.s2.pop()


class CallStackQueue:

    def __init__(self):
        self.s = Stack()
        self.size = 0

    def enqueue(self, value: Any = None):
        self.s.push(value)
        self.size += 1

    def dequeue(self) -> Union[Any, None]:
        x = self.s.pop()
        if not self.s.size:
            self.size = max(0, self.size - 1)
            return x

        item = self.dequeue()

        self.s.push(x)
        self.size -= 1
        return item

