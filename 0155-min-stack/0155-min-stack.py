class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # keeps track of minimums

    def push(self, value: int) -> None:
        self.stack.append(value)
        # push to min_stack if it's empty or value <= current min
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None
