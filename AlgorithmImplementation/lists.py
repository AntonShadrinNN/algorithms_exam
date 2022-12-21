from typing import Any


class Node:

    def __init__(self, value: Any):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def __getitem__(self, item):
        if item >= self.__size or item < 0:
            raise IndexError("List index out of range!")

        value = self.__head
        for _ in range(item):
            value = value.next

        return value.value

    def __str__(self):
        result = ""
        cur_node = self.__head
        while cur_node:
            result += f'{cur_node.value} '
            cur_node = cur_node.next
        return result

    def insert_at_end(self, value: Any):
        if not self.__head:
            self.__size += 1
            self.__head = Node(value)
            self.__tail = self.__head
            return

        cur_node = self.__head
        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = Node(value)
        cur_node.next.prev = cur_node
        self.__tail = cur_node.next
        self.__tail.prev = cur_node
        self.__size += 1

    def reverse_doubly_linked_list(self):
        p = self.__head
        self.__head, self.__tail = self.__tail, self.__head

        while p:
            p.prev, p.next = p.next, p.prev
            p = p.prev


l = DoublyLinkedList()
l.insert_at_end(12)
l.insert_at_end(123)
l.insert_at_end(124)
l.reverse_doubly_linked_list()
print(l)