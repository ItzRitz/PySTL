from error import EmptyStackError
from structures.node_structure.ll_node import Node

class Stack:
    def __init__(self):
        self.__bottom = None
        self.__top = None
        self.__size = 0
    
    def empty(self):
        """Checks if the stack is empty"""
        return self.__size == 0
    
    def push(self, val):
        """Pushes and element at the top of stack"""
        new_node = Node(val)

        if self.empty():
            self.__bottom = new_node
            self.__top = new_node
        else:
            self.__top.next = new_node
            new_node.prev = self.__top

            self.__top = new_node

        self.__size += 1

    def pop(self):
        """Pops and returns the element from the top of stack"""
        if not self.empty():
            
            popped_node = self.__top
            self.__size -= 1
            if self.__top.prev is None:
                self.__top = None
                self.__bottom = None
                return popped_node.val
            new_top = self.__top.prev

            new_top.next = None
            self.__top.prev = None
            self.__top = new_top

            return popped_node.val
        else:
            raise EmptyStackError
    
    def top(self):
        """Retuns the element from the top of the stack"""
        if not self.empty():
            return self.__top.val
        else:
            raise EmptyStackError
    
    def size(self):
        """Returns the size of the stack"""
        return self.__size
    
    def __len__(self):
        return self.__size