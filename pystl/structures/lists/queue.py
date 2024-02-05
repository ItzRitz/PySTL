from error import EmptyQueueError
from structures.node_structure.ll_node import Node

class Queue:
    def __init__(self):
        self.__front = None
        self.__back = None
        self.__size = 0
    
    def empty(self):
        """Checks if the queue is empty"""
        return self.__front == None
    
    def push(self, val):
        """Pushes an element at back of the queue"""
        new_node = Node(val)

        if self.empty():
            self.__front = new_node
            self.__back = new_node
        else:
            self.__back.next = new_node
            new_node.prev = self.__back

            self.__back = new_node

        self.__size += 1
    
    def pop(self):
        """Removes and returns an element from the front of the queue"""
        if self.empty():
            raise EmptyQueueError
        
        popped_node = self.__front
        self.__size -= 1

        if self.__front.next is None:
            self.__front = None
            self.__back = None
            
            return popped_node.val
        
        new_head = self.__front.next
        self.__front.next = None
        new_head.prev = None
        self.__front = new_head

        return popped_node.val
    
    def front(self):
        """Returns the element from the front of the queue"""
        if not self.empty():
            return self.__front.val
        else:
            raise EmptyQueueError
        
    def back(self):
        """Returns the element from the back of the queue"""
        if not self.empty():
            return self.__back.val
        else:
            raise EmptyQueueError
    
    def size(self):
        """Returns the size of the queue"""
        return self.size
    
    def __len__(self):
        return self.size