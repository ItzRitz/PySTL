from error import EmptyListError
from models.abstract_list import AbstractList
from structures.node_structure.ll_node import Node


class LinkedList(AbstractList):
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        self.size = 0
        if lst is not None:
            for val in lst:
                self.append(val)

    def append(self, val):
        """Pushes and element at the end of the linked list"""
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, val):
        """Pushes and element at the head/front of the linked list"""

        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def insert(self, val, index):
        """Pushes and element at a specific index in the linked list"""
        if index < 0 or index > self.size:
            raise IndexError(f"index {index} out of bounds")

        if index == 0:
            self.prepend(val)
            return
        elif index == self.size:
            self.append(val)
            return

        new_node = Node(val)
        current = self.head

        for _ in range(index):
            current = current.next

        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node

        self.size += 1

    def at(self, index):
        """Returns the value at a specific index in the linked list"""
        if index < 0 or index >= self.size:
            raise IndexError(f"index {index} out of bounds")

        current = self.head

        for _ in range(index):
            current = current.next

        return current.val

    def pop(self, index=None):
        """Pops and returns and element from the end of the 
        linkned list in case an in case an index is not provided.
        In case an index is provided, pops and returns element from that index"""
        if index is None:
            if self.size == 0:
                raise EmptyListError

            popped_value = self.tail.val
            self.tail = self.tail.prev

            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            if index < 0 or index >= self.size:
                raise IndexError(f"index {index} out of bounds")

            current = self.head

            for _ in range(index):
                current = current.next

            popped_value = current.val

            if current.prev:
                current.prev.next = current.next
            else:
                # If popping the first element, update the head
                self.head = current.next

            if current.next:
                current.next.prev = current.prev
            else:
                # If popping the last element, update the tail
                self.tail = current.prev

        self.size -= 1
        return popped_value

    def remove(self, val):
        """Removes a single instance of the value passed from the list"""
        current = self.head

        while current:
            if current.val == val:
                if current.prev:
                    current.prev.next = current.next
                else:
                    # If removing the first element, update the head
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    # If removing the last element, update the tail
                    self.tail = current.prev

                self.size -= 1
                return

            current = current.next

    def empty(self):
        """Checks if the list is empty"""
        return self.size == 0

    def __len__(self):
        return self.size

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            data = self.current.val
            self.current = self.current.next
            return data
        else:
            raise StopIteration
