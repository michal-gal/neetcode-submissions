class MinStack:

    def __init__(self):
        self.stack = []
        self.min_list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_list:
            if self.min_list[-1] > val:
                self.min_list.append(val)
            else:
                self.min_list.append(self.min_list[-1])
        else:
            self.min_list.append(val)


    def pop(self) -> None:
        self.min_list.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack:
            return self.min_list[-1]
        return 0
        
