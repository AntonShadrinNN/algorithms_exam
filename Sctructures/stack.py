from typing import Any, Union

__all__ = ('Stack',)


class Node:

    def __init__(self, value: Any = None):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value: Any):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self) -> Union[Any, None]:
        if self.top:
            value = self.top.value
            self.top = self.top.next
            self.size -= 1
            return value

