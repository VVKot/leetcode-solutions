"""
T: O(1) everything
S: O(N)

The only trick case is storing a minimum number. The basic idea is to store it
on the push and modify on pop, but that will lead to the linear runtime of pop.
To avoid that, when we add new minimum number X, we also record previously seen
minimum number Y >= X, and assign it to a global minimum if X gets popped.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = float('inf')

    def push(self, x: int) -> None:
        if x <= self.min_num:
            self.stack.append(self.min_num)
            self.min_num = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min_num:
            self.min_num = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num
