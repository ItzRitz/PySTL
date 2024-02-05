from abc import ABC, abstractmethod


class AbstractTree(ABC):
    @abstractmethod
    def push(self, val):
        pass

    @abstractmethod
    def pop(self, val):
        pass

    @abstractmethod
    def empty(self):
        pass
