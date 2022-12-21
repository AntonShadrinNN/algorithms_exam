from typing import Any, Union


class Node:

    def __init__(self, value: Any = None):
        self.value = value
        self.next = None


class CustomQueue:

    def __init__(self):
        self.top = None
        self.size = 0

    def enqueue(self, value: Any):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
            self.size += 1
            return

        cur_node = self.top
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def dequeue(self) -> Union[Any, None]:
        if self.top:
            value = self.top.value
            self.size -= 1
            self.top = self.top.next
            return value
