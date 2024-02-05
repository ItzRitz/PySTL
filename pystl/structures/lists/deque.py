from error import EmptyDequeError
from structures.node_structure.ll_node import Node


class Deque:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__size = 0

    def empty(self):
        """Checks if the deque is empty or not"""
        return self.__front is None

    def push_front(self, val):
        """Inserts a new element at the front of the deque"""
        new_node = Node(val)
        if self.empty():
            self.__front = new_node
            self.__rear = new_node
        else:
            new_node.next = self.__front
            self.__front.prev = new_node
            self.__front = new_node

        self.__size += 1

    def push_back(self, val):
        """Inserts a new element at the back of the deque"""
        new_node = Node(val)
        if self.empty():
            self.__front = new_node
            self.__rear = new_node
        else:
            new_node.prev = self.__rear
            self.__rear.next = new_node
            self.__rear = new_node

        self.__size += 1

    def pop_front(self):
        """Pops and returns an element from the front of the deque"""
        if not self.empty():
            removed_item = self.__front.data
            self.__front = self.__front.next
            if self.__front is None:
                self.__rear = None
            else:
                self.__front.prev = None
            self.__size -= 1
            return removed_item
        else:
            raise EmptyDequeError

    def pop_back(self):
        """Pops and returns an element from the back of the deque"""
        if not self.empty():
            removed_item = self.__rear.data
            self.__rear = self.__rear.prev
            if self.__rear is None:
                self.__front = None
            else:
                self.__rear.next = None
            self.__size -= 1
            return removed_item
        else:
            raise EmptyDequeError

    def front(self):
        """Returns the value at the front of the deque"""
        if not self.empty():
            return self.__front.val
        else:
            raise EmptyDequeError

    def back(self):
        """Returns the value at the end of the deque"""
        if not self.empty():
            return self.__rear.val
        else:
            raise EmptyDequeError

    def size(self):
        """Returns the size of the deque"""
        return self.__size
    
    def __len__(self):
        return self.__size