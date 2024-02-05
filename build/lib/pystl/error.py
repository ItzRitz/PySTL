class EmptyListError(Exception):
    def __init__(self) -> None:
        self.message = "Empty list"
        super().__init__(self.message)

class EmptyTreeError(Exception):
    def __init__(self) -> None:
        self.message = "Empty tree"
        super().__init__(self.message)

class EmptyStackError(Exception):
    def __init__(self) -> None:
        self.message = "Empty stack"
        super().__init__(self.message)

class EmptyQueueError(Exception):
    def __init__(self) -> None:
        self.message = "Empty queue"
        super().__init__(self.message)

class EmptyDequeError(Exception):
    def __init__(self) -> None:
        self.message = "Empty deque"
        super().__init__(self.message)

class ElementNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(args)

