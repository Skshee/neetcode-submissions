class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        value = self.arr[-1]
        return value

    def getMin(self) -> int:
        minVal = min(self.arr)
        return minVal
