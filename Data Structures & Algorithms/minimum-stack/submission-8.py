class MinStack:

    def __init__(self):
        self.stack = []
        self.min_dict = {}
        self.minimum = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_dict:
            self.minimum = val
        elif self.minimum > val:
            self.minimum = val
        self.min_dict[len(self.stack)] = self.minimum

    def pop(self) -> None:
        self.min_dict.popitem()
        if self.min_dict:
            self.minimum = self.min_dict[len(self.min_dict)]
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack:
            return self.minimum
        return 0
        
