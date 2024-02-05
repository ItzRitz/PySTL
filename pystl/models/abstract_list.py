from abc import ABC, abstractmethod


class AbstractList(ABC):
    @abstractmethod
    def append(self, val):
        pass

    @abstractmethod
    def prepend(self, val):
        pass

    @abstractmethod
    def insert(self, val, index):
        pass

    @abstractmethod
    def at(self, index):
        pass

    @abstractmethod
    def pop(self, index):
        pass

    @abstractmethod
    def remove(self, val):
        pass

    @abstractmethod
    def empty(self):
        pass
